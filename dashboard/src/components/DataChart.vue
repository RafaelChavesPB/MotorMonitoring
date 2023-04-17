<template>
  <v-card color="#525977" class="card" rounded="10">
    <canvas ref="chart"> </canvas>
  </v-card>
</template>

<script>
import { Chart, registerables } from "chart.js";
export default {
  props: ["chartData"],
  data() {
    return {
      chart: null,
    };
  },
  watch: {
    chartData(){
        if(this.chart){
            this.chart.data.labels = this.chartData.labels
            this.updateDatasets(this.chartData.datasets)
            this.chart.update()
        }
    }
  },
  methods:{
    updateDatasets(newDatasets){
      for(let i in newDatasets){
        this.chart.data.datasets[i].data = newDatasets[i].data;
      }
    }
  },
  mounted() {
    const ctx = this.$refs.chart;

    Chart.register(...registerables);
    this.chart = new Chart(ctx, {
      type: "line",
      data: this.chartData,
      responsive: true,
      options:{
          scales: {
            y: {
              beginAtZero: true,
            },
            x: {
              ticks: {
                display: false,
              },
            },
          },
      }
    });
  },
};
</script>

<style>
.card {
    margin: 10px;
    padding: 20px;    
}
</style>