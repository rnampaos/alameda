package app

import (
	"github.com/containers-ai/alameda/apiserver/pkg/probe"
	"github.com/spf13/cobra"
	"os"
)

const (
	probeTypeLiveness  = "liveness"
	probeTypeReadiness = "readiness"
)

var (
	probeType string

	ProbeCmd = &cobra.Command{
		Use:   "probe",
		Short: "probe alameda apiserver",
		Long:  "",
		Run: func(cmd *cobra.Command, args []string) {
			initConfig()
			initLogger()
			setLoggerScopesWithConfig(*config.Log)
			startProbing()
		},
	}
)

func init() {
	parseProbeFlag()
}

func parseProbeFlag() {
	ProbeCmd.Flags().StringVar(&probeType, "type", probeTypeReadiness, "The probe type for apiserver.")
}

func startProbing() {
	if probeType == probeTypeLiveness {
		probe.LivenessProbe(&probe.LivenessProbeConfig{
			BindAddr: config.BindAddress,
		})
	} else if probeType == probeTypeReadiness {
		probe.ReadinessProbe(&probe.ReadinessProbeConfig{
			BindAddr: config.BindAddress,
		})
	} else {
		scope.Errorf("Probe type does not supports %s, please try %s or %s.", probeType, probeTypeLiveness, probeTypeReadiness)
		os.Exit(1)
	}
}
