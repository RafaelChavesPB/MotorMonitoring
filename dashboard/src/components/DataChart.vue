<template>
  <div>
    <LineChart id="my-chart-id" :options="chartOptions" :data="chartData" />
  </div>
</template>

<script>
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "DataChart",
  components: { LineChart: Line },
  props: ["values", "time", "label"],
  data() {
    return {
      chartOptions: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    };
  },
  computed: {
    chartData() {
      return {
        datasets: [
          {
            label: this.label,
            data: this.values,
            cubicInterpolationMode: "monotone",
            tension: 0.4,
          },
        ],
        labels: this.time,
      };
    },
  },
};
</script>