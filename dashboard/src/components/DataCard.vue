<template>
  <div class="container">
    <div class="card">
      <div class="title"> {{label}}</div>
      <hr style="color: white" />
      <div class="content">
        <div class="values">
          <div class="value">
            <label> Média </label>
            <span>
              {{ mean.toFixed(1) }}
            </span>
          </div>
          <div class="value">
            <label> Max </label>
            <span>
              {{ max.toFixed(1) }}
            </span>
          </div>
          <div class="value">
            <label> Min </label>
            <span>
              {{ min.toFixed(1) }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["values","updated_at", "label"],
  watch: {
    values() {
      if (this.values.length) {
        let sum = 0;
        this.min = this.values[0];
        this.max = this.values[0];
        this.points = this.values.length;
        for (let it of this.values) {
          this.max = Math.max(this.max, it);
          this.min = Math.min(this.min, it);
          sum += it;
        }
        this.max = this.max
        this.mean = sum / this.points;
      }
    },
  },
  data() {
    return {
      max: 0,
      min: 0,
      points: 0,
      mean: 0,
    };
  },
};
</script>

<style scoped>
.container {
  width: 33%;
  height: 50%;
  padding: 10px;
}
.card {
    height: 100%;
  background-color: #525977;
  border-radius: 10px;
  padding: 20px;
}
.title {
  height: 20%;
  font-size: 1.8rem;
  font-weight: 500;
  color: white;
}

.values {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 10px;
  height: 100%;
}

.value {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

label {
  color: white;
  font-size: 0.8rem;
  font-weight: 600;
}

span {
  color: white;
  font-size: 2.3rem;
  font-weight: 500;
}

.content {
  height: 80%;
  flex-direction: column;
  display: flex;
  justify-content: center;
}
</style>