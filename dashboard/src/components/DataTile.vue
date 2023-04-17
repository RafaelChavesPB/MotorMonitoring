<template>
    <div class="dashtile">
        <DataCard :values="measurements.power" label="Potência (W)"/>
        <DataCard :values="measurements.voltage" label="Tensão (V)"/>
        <DataCard :values="measurements.current" label="Corrente (A)" />
    </div>
</template>
<script>
import DataCard from "./DataCard.vue";

export default {
  components: { DataCard },
  props: ["measurements"]
  
};
</script>

<style scoped>
 .dashtile{
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  justify-content: space-around;
 }
</style>