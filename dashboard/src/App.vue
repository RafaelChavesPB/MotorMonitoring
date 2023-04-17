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
  background-color: #323C57;
  height: 100vh;
}
</style>
