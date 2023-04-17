<template>
  <div class="container">
    <div class="card">
      <canvas ref="chart"> </canvas>
    </div>
  </div>
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
    chartData() {
      if (this.chart) {
        this.chart.data.labels = this.chartData.labels;
        this.updateDatasets(this.chartData.datasets);
        this.chart.update();
      }
    },
  },
  methods: {
    updateDatasets(newDatasets) {
      for (let i in newDatasets) {
        this.chart.data.datasets[i].data = newDatasets[i].data;
      }
    },
  },
  mounted() {
    const ctx = this.$refs.chart;
    Chart.defaults.color = "#FFFFFF";
    Chart.defaults.font.size = 15;
    Chart.register(...registerables);
    this.chart = new Chart(ctx, {
      type: "line",
      data: this.chartData,
      options: {
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              color: "white",
              font: { size: 15 },
            },
          },
          x: {
            ticks: {
              display: false,
            },
          },
        },
      },
    });
  },
};
</script>

<style scoped>
.container {
  padding: 10px;
}

.card {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #525977;
    border-radius: 10px;
    padding: 10px;
  }
</style>