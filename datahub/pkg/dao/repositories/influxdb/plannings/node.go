package plannings

import (
	EntityInfluxPlanning "github.com/containers-ai/alameda/datahub/pkg/dao/entities/influxdb/plannings"
	RepoInflux "github.com/containers-ai/alameda/datahub/pkg/dao/repositories/influxdb"
	DBCommon "github.com/containers-ai/alameda/internal/pkg/database/common"
	InternalInflux "github.com/containers-ai/alameda/internal/pkg/database/influxdb"
	ApiPlannings "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/plannings"
	ApiResources "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/resources"
	"github.com/golang/protobuf/ptypes"
	"github.com/golang/protobuf/ptypes/timestamp"
	InfluxClient "github.com/influxdata/influxdb/client/v2"
	"strconv"
	"time"
)

type NodeRepository struct {
	influxDB *InternalInflux.InfluxClient
}

func NewNodeRepository(influxDBCfg *InternalInflux.Config) *NodeRepository {
	return &NodeRepository{
		influxDB: &InternalInflux.InfluxClient{
			Address:  influxDBCfg.Address,
			Username: influxDBCfg.Username,
			Password: influxDBCfg.Password,
		},
	}
}

func (c *NodeRepository) CreatePlannings(plannings []*ApiPlannings.NodePlanning) error {
	points := make([]*InfluxClient.Point, 0)

	for _, planning := range plannings {
		nodePlanningType := planning.GetNodePlanningType()

		if nodePlanningType == ApiPlannings.ControllerPlanningType_CPT_PRIMITIVE {
			planningSpec := planning.GetNodePlanningSpec()

			tags := map[string]string{
				EntityInfluxPlanning.NodePlanningType: planning.GetPlanningType().String(),
				EntityInfluxPlanning.NodeName:         planning.GetObjectMeta().GetName(),
				EntityInfluxPlanning.NodeType:         ApiPlannings.ControllerPlanningType_CPT_PRIMITIVE.String(),
			}

			fields := map[string]interface{}{
				EntityInfluxPlanning.NodeCurrentReplicas: planningSpec.GetCurrentReplicas(),
				EntityInfluxPlanning.NodeDesiredReplicas: planningSpec.GetDesiredReplicas(),
				EntityInfluxPlanning.NodeCreateTime:      planningSpec.GetCreateTime().GetSeconds(),
				EntityInfluxPlanning.NodeKind:            planning.GetKind().String(),

				EntityInfluxPlanning.NodeCurrentCPURequest: planningSpec.GetCurrentCpuRequests(),
				EntityInfluxPlanning.NodeCurrentMEMRequest: planningSpec.GetCurrentMemRequests(),
				EntityInfluxPlanning.NodeCurrentCPULimit:   planningSpec.GetCurrentCpuLimits(),
				EntityInfluxPlanning.NodeCurrentMEMLimit:   planningSpec.GetCurrentMemLimits(),
				EntityInfluxPlanning.NodeDesiredCPULimit:   planningSpec.GetDesiredCpuLimits(),
				EntityInfluxPlanning.NodeDesiredMEMLimit:   planningSpec.GetDesiredMemLimits(),
				EntityInfluxPlanning.NodeTotalCost:         planningSpec.GetTotalCost(),
			}

			pt, err := InfluxClient.NewPoint(string(Node), tags, fields, time.Unix(planningSpec.GetTime().GetSeconds(), 0))
			if err != nil {
				scope.Error(err.Error())
			}

			points = append(points, pt)

		} else if nodePlanningType == ApiPlannings.ControllerPlanningType_CPT_K8S {
			planningSpec := planning.GetNodePlanningSpecK8S()

			tags := map[string]string{
				EntityInfluxPlanning.NodePlanningType: planning.GetPlanningType().String(),
				EntityInfluxPlanning.NodeName:         planning.GetObjectMeta().GetName(),
				EntityInfluxPlanning.NodeType:         ApiPlannings.ControllerPlanningType_CPT_K8S.String(),
			}

			fields := map[string]interface{}{
				EntityInfluxPlanning.NodeCurrentReplicas: planningSpec.GetCurrentReplicas(),
				EntityInfluxPlanning.NodeDesiredReplicas: planningSpec.GetDesiredReplicas(),
				EntityInfluxPlanning.NodeCreateTime:      planningSpec.GetCreateTime().GetSeconds(),
				EntityInfluxPlanning.NodeKind:            planning.GetKind().String(),
			}

			pt, err := InfluxClient.NewPoint(string(Node), tags, fields, time.Unix(planningSpec.GetTime().GetSeconds(), 0))
			if err != nil {
				scope.Error(err.Error())
			}

			points = append(points, pt)
		}
	}

	err := c.influxDB.WritePoints(points, InfluxClient.BatchPointsConfig{
		Database: string(RepoInflux.Planning),
	})

	if err != nil {
		scope.Error(err.Error())
		return err
	}

	return nil
}

func (c *NodeRepository) ListPlannings(in *ApiPlannings.ListNodePlanningsRequest) ([]*ApiPlannings.NodePlanning, error) {
	influxdbStatement := InternalInflux.Statement{
		Measurement:    Node,
		QueryCondition: DBCommon.BuildQueryConditionV1(in.GetQueryCondition()),
	}

	planningType := in.GetPlanningType().String()
	ctlPlanningType := in.GetCtlPlanningType().String()
	kind := in.GetKind().String()

	for _, objMeta := range in.GetObjectMeta() {
		name := objMeta.GetName()

		keyList := []string{
			EntityInfluxPlanning.NodeName,
			EntityInfluxPlanning.NodeKind,
		}
		valueList := []string{name, kind}

		if ctlPlanningType != ApiPlannings.ControllerPlanningType_CPT_UNDEFINED.String() {
			keyList = append(keyList, EntityInfluxPlanning.NodeType)
			valueList = append(valueList, ctlPlanningType)
		}

		if planningType != ApiPlannings.PlanningType_PT_UNDEFINED.String() {
			keyList = append(keyList, EntityInfluxPlanning.NodePlanningType)
			valueList = append(valueList, planningType)
		}

		tempCondition := influxdbStatement.GenerateCondition(keyList, valueList, "AND")
		influxdbStatement.AppendWhereClauseDirectly("OR", tempCondition)
	}

	influxdbStatement.AppendWhereClauseFromTimeCondition()
	influxdbStatement.SetOrderClauseFromQueryCondition()
	influxdbStatement.SetLimitClauseFromQueryCondition()

	cmd := influxdbStatement.BuildQueryCmd()

	results, err := c.influxDB.QueryDB(cmd, string(RepoInflux.Planning))
	if err != nil {
		return make([]*ApiPlannings.NodePlanning, 0), err
	}

	influxdbRows := InternalInflux.PackMap(results)
	plannings := c.getPlanningsFromInfluxRows(influxdbRows)

	return plannings, nil
}

func (c *NodeRepository) getPlanningsFromInfluxRows(rows []*InternalInflux.InfluxRow) []*ApiPlannings.NodePlanning {
	plannings := make([]*ApiPlannings.NodePlanning, 0)

	for _, influxdbRow := range rows {
		for _, data := range influxdbRow.Data {
			currentReplicas, _ := strconv.ParseInt(data[EntityInfluxPlanning.NodeCurrentReplicas], 10, 64)
			desiredReplicas, _ := strconv.ParseInt(data[EntityInfluxPlanning.NodeDesiredReplicas], 10, 64)
			createTime, _ := strconv.ParseInt(data[EntityInfluxPlanning.NodeCreateTime], 10, 64)

			t, _ := time.Parse(time.RFC3339, data[EntityInfluxPlanning.NodeTime])
			tempTime, _ := ptypes.TimestampProto(t)

			currentCpuRequests, _ := strconv.ParseFloat(data[EntityInfluxPlanning.NodeCurrentCPURequest], 64)
			currentMemRequests, _ := strconv.ParseFloat(data[EntityInfluxPlanning.NodeCurrentMEMRequest], 64)
			currentCpuLimits, _ := strconv.ParseFloat(data[EntityInfluxPlanning.NodeCurrentCPULimit], 64)
			currentMemLimits, _ := strconv.ParseFloat(data[EntityInfluxPlanning.NodeCurrentMEMLimit], 64)
			desiredCpuLimits, _ := strconv.ParseFloat(data[EntityInfluxPlanning.NodeDesiredCPULimit], 64)
			desiredMemLimits, _ := strconv.ParseFloat(data[EntityInfluxPlanning.NodeDesiredMEMLimit], 64)
			totalCost, _ := strconv.ParseFloat(data[EntityInfluxPlanning.NodeTotalCost], 64)

			var ctlPlanningType ApiPlannings.ControllerPlanningType
			if tempType, exist := data[EntityInfluxPlanning.NodeType]; exist {
				if value, ok := ApiPlannings.ControllerPlanningType_value[tempType]; ok {
					ctlPlanningType = ApiPlannings.ControllerPlanningType(value)
				}
			}

			var planningKind ApiResources.Kind
			if tempKind, exist := data[EntityInfluxPlanning.NodeKind]; exist {
				if value, ok := ApiResources.Kind_value[tempKind]; ok {
					planningKind = ApiResources.Kind(value)
				}
			}

			if ctlPlanningType == ApiPlannings.ControllerPlanningType_CPT_PRIMITIVE {
				tempPlanning := &ApiPlannings.NodePlanning{
					ObjectMeta: &ApiResources.ObjectMeta{
						Name: data[string(EntityInfluxPlanning.NodeName)],
					},
					Kind:             planningKind,
					PlanningType:     ApiPlannings.PlanningType(ApiPlannings.PlanningType_value[data[string(EntityInfluxPlanning.NodePlanningType)]]),
					NodePlanningType: ctlPlanningType,
					NodePlanningSpec: &ApiPlannings.ControllerPlanningSpec{
						CurrentReplicas: int32(currentReplicas),
						DesiredReplicas: int32(desiredReplicas),
						Time:            tempTime,
						CreateTime: &timestamp.Timestamp{
							Seconds: createTime,
						},
						CurrentCpuRequests: currentCpuRequests,
						CurrentMemRequests: currentMemRequests,
						CurrentCpuLimits:   currentCpuLimits,
						CurrentMemLimits:   currentMemLimits,
						DesiredCpuLimits:   desiredCpuLimits,
						DesiredMemLimits:   desiredMemLimits,
						TotalCost:          totalCost,
					},
				}

				plannings = append(plannings, tempPlanning)

			} else if ctlPlanningType == ApiPlannings.ControllerPlanningType_CPT_K8S {
				tempPlanning := &ApiPlannings.NodePlanning{
					ObjectMeta: &ApiResources.ObjectMeta{
						Name: data[string(EntityInfluxPlanning.NodeName)],
					},
					Kind:             planningKind,
					PlanningType:     ApiPlannings.PlanningType(ApiPlannings.PlanningType_value[data[string(EntityInfluxPlanning.NodePlanningType)]]),
					NodePlanningType: ctlPlanningType,
					NodePlanningSpecK8S: &ApiPlannings.ControllerPlanningSpecK8S{
						CurrentReplicas: int32(currentReplicas),
						DesiredReplicas: int32(desiredReplicas),
						Time:            tempTime,
						CreateTime: &timestamp.Timestamp{
							Seconds: createTime,
						},
					},
				}

				plannings = append(plannings, tempPlanning)
			}
		}
	}

	return plannings
}