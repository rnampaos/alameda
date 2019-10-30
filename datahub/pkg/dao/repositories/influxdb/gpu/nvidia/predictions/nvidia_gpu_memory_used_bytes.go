package predictions

import (
	EntityInfluxGpuPrediction "github.com/containers-ai/alameda/datahub/pkg/dao/entities/influxdb/gpu/nvidia/predictions"
	DaoGpu "github.com/containers-ai/alameda/datahub/pkg/dao/interfaces/gpu/influxdb"
	RepoInflux "github.com/containers-ai/alameda/datahub/pkg/dao/repositories/influxdb"
	DatahubUtils "github.com/containers-ai/alameda/datahub/pkg/utils"
	DBCommon "github.com/containers-ai/alameda/internal/pkg/database/common"
	InternalInflux "github.com/containers-ai/alameda/internal/pkg/database/influxdb"
	InternalInfluxModels "github.com/containers-ai/alameda/internal/pkg/database/influxdb/models"
	InfluxClient "github.com/influxdata/influxdb/client/v2"
	"github.com/pkg/errors"
	"strconv"
)

type MemoryUsedBytesRepository struct {
	influxDB *InternalInflux.InfluxClient
}

func NewMemoryUsedBytesRepositoryWithConfig(cfg InternalInflux.Config) *MemoryUsedBytesRepository {
	return &MemoryUsedBytesRepository{
		influxDB: InternalInflux.NewClient(&cfg),
	}
}

func (r *MemoryUsedBytesRepository) CreatePredictions(predictions []*DaoGpu.GpuPrediction) error {
	points := make([]*InfluxClient.Point, 0)

	for _, prediction := range predictions {
		granularity := int64(30)
		if prediction.Granularity != 0 {
			granularity = prediction.Granularity
		}

		for _, metric := range prediction.Metrics {
			// Parse float string to value
			valueInFloat64, err := DatahubUtils.StringToFloat64(metric.Value)
			if err != nil {
				return errors.Wrap(err, "failed to parse string to float64")
			}

			// Pack influx tags
			tags := map[string]string{
				EntityInfluxGpuPrediction.MemoryUsedBytesHost:        prediction.Metadata.Host,
				EntityInfluxGpuPrediction.MemoryUsedBytesName:        prediction.Name,
				EntityInfluxGpuPrediction.MemoryUsedBytesUuid:        prediction.Uuid,
				EntityInfluxGpuPrediction.MemoryUsedBytesGranularity: strconv.FormatInt(granularity, 10),
			}

			// Pack influx fields
			fields := map[string]interface{}{
				EntityInfluxGpuPrediction.MemoryUsedBytesModelId:      metric.ModelId,
				EntityInfluxGpuPrediction.MemoryUsedBytesPredictionId: metric.PredictionId,
				EntityInfluxGpuPrediction.MemoryUsedBytesMinorNumber:  prediction.Metadata.MinorNumber,
				EntityInfluxGpuPrediction.MemoryUsedBytesValue:        valueInFloat64,
			}

			// Add to influx point list
			point, err := InfluxClient.NewPoint(string(MemoryUsedBytes), tags, fields, metric.Timestamp)
			if err != nil {
				return errors.Wrap(err, "failed to instance influxdb data point")
			}
			points = append(points, point)
		}
	}

	// Batch write influxdb data points
	err := r.influxDB.WritePoints(points, InfluxClient.BatchPointsConfig{
		Database: string(RepoInflux.GpuPrediction),
	})
	if err != nil {
		return errors.Wrap(err, "failed to batch write influxdb data points")
	}

	return nil
}

func (r *MemoryUsedBytesRepository) ListPredictions(host, minorNumber, modelId, predictionId, granularity string, condition *DBCommon.QueryCondition) ([]*EntityInfluxGpuPrediction.MemoryUsedBytesEntity, error) {
	entities := make([]*EntityInfluxGpuPrediction.MemoryUsedBytesEntity, 0)

	influxdbStatement := InternalInflux.Statement{
		QueryCondition: condition,
		Measurement:    MemoryUsedBytes,
		GroupByTags:    []string{"host", "uuid"},
	}

	influxdbStatement.AppendWhereClauseFromTimeCondition()
	influxdbStatement.AppendWhereClause(EntityInfluxGpuPrediction.MemoryUsedBytesHost, "=", host)
	influxdbStatement.AppendWhereClause(EntityInfluxGpuPrediction.MemoryUsedBytesMinorNumber, "=", minorNumber)
	influxdbStatement.AppendWhereClause(EntityInfluxGpuPrediction.MemoryUsedBytesModelId, "=", modelId)
	influxdbStatement.AppendWhereClause(EntityInfluxGpuPrediction.MemoryUsedBytesPredictionId, "=", predictionId)
	influxdbStatement.AppendWhereClause(EntityInfluxGpuPrediction.MemoryUsedBytesGranularity, "=", granularity)
	influxdbStatement.SetOrderClauseFromQueryCondition()
	influxdbStatement.SetLimitClauseFromQueryCondition()
	cmd := influxdbStatement.BuildQueryCmd()

	response, err := r.influxDB.QueryDB(cmd, string(RepoInflux.GpuPrediction))
	if err != nil {
		return entities, errors.Wrap(err, "failed to list nvidia gpu memory used bytes predictions")
	}

	results := InternalInfluxModels.NewInfluxResults(response)
	for _, result := range results {
		for i := 0; i < result.GetGroupNum(); i++ {
			group := result.GetGroup(i)
			for j := 0; j < group.GetRowNum(); j++ {
				entity := EntityInfluxGpuPrediction.NewMemoryUsedBytesEntityFromMap(group.GetRow(j))
				entities = append(entities, &entity)
			}
		}
	}

	return entities, nil
}