<template>
  <div class="footer">
    <span class="footer__text text-white">win_plus_ners</span>
  </div>
</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";

export default {
  name: "Footer",
  mixins: [goToSomewhere],
}
</script>

<style scoped>
  .footer {
    background-color: Blue;
    text-align: center;
    padding: 4px 0;
  }
</style>