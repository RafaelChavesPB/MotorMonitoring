<template>
  <div justify="center" class="dashroot">
    <DataChart
      class="tile"
      :chartData="chartData(power, time, 'Potência (W)')"
    />
    <DataChart
      class="tile"
      :chartData="chartData(current, time, 'Corrente (A)')"
    />
    <DataChart
      class="tile"
      :chartData="chartData(voltage, time, 'Tensão (V)')"
    />
    <DataTile class="tile" :measurements="measurements" />
  </div>
</template>

<script>
import DataChart from "./DataChart.vue";
import DataTile from "./DataTile.vue";
import io from "socket.io-client";
export default {
  name: "DataDashboard",
  components: { DataChart, DataTile },
  data() {
    return {
      socket: {},
      voltage: [],
      current: [],
      power:[],
      time: [],
    };
  },
  computed:{
    measurements(){
      return {voltage:this.voltage, current:this.current, power:this.power}
    }
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
        this.power.splice(0, 1);
        this.time.splice(0, 1);
      }
      this.current.push(params.current);
      this.voltage.push(params.voltage);
      this.power.push(params.current * params.voltage)
      this.time.push(params.time );
    },
    chartData(values, labels, legend) {
      return {
        datasets: [
          {
            label: legend,
            data: values,
            cubicInterpolationMode: "monotone",
            borderColor: "white",
            tension: 0.4,
          },
        ],
        labels: labels,
      };
    },
  },
};
</script>

<style scoped>
.tile {
  width: 50%;
  height: 50%;
}

.dashroot {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  justify-content: space-around;
  height: 100%;
}
</style>
