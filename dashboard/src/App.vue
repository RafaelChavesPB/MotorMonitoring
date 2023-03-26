<template>
  <div id="app">
    <DataDashboard />
  </div>
</template>

<script>
import DataDashboard from "./components/DataDashboard.vue";
export default {
  name: "App",
  components: {
    DataDashboard,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
