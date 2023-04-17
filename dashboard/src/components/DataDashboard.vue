<template>
  <v-row no-gutters>
    <v-col>
      <DataChart  :chartData="chartData(current, time, 'Corrente')"/>
    </v-col>
    <v-col>
      <DataChart  :chartData="chartData(voltage, time, 'Tensão')"/>
    </v-col>
  </v-row>
</template>

<script>
import DataChart from "./DataChart.vue";
import io from "socket.io-client";
export default {
  name: "DataDashboard",
  components: { DataChart },
  data() {
    return {
      socket: {},
      voltage: [],
      current: [],
      time: [],
    };
  },
  created() {
    this.socket = io("http://localhost:5000");
  },
  mounted() {
    this.socket.on("incoming_data", (params) => {
      this.update(params);
    });
  },
  methods: {
    update(params) {
      if (this.time.length >= 30) {
        this.current.splice(0, 1);
        this.voltage.splice(0, 1);
        this.time.splice(0, 1);
      }
      this.current.push(params.current);
      this.voltage.push(params.voltage);
      this.time.push(params.time);
    },
    chartData(values, labels, legend) {
      return {
        datasets: [
          {
            label: legend,
            data: values,
            cubicInterpolationMode: "monotone",
            tension: 0.4,
          },
        ],
        labels: labels,
      };
    },
  },
};
</script>
