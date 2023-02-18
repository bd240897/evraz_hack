<template>
  <div class="page_nav mb-2">
    <b-navbar toggleable type="dark" variant="primary">
      <b-navbar-brand v-on:click="goToFirst" class="ms-2 text-white fw-bold" href="#">Евраз</b-navbar-brand>

      <b-navbar-toggle class="me-2" target="navbar-toggle-collapse">


        <template #default="{ expanded }">
          &#128523;
<!--          <b-icon v-if="expanded" icon="chevron-bar-up">&#128559;</b-icon>-->
<!--          <b-icon v-else icon="chevron-bar-down">&#128523;</b-icon>-->
        </template>
      </b-navbar-toggle>

      <b-collapse id="navbar-toggle-collapse" is-nav>
        <b-navbar-nav class="ms-auto text-white">
          <b-nav-item to="/first-screen/" class="ms-2" href="#">First</b-nav-item>
          <b-nav-item to="/second-screen/1/" class="ms-2" href="#">Second</b-nav-item>
          <b-nav-item to="/third-screen/" class="ms-2" href="#">Third</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>


<script>
import goToSomewhere from "@/mixins/goToSomewhere";

export default {
  name: "Navbar",
  mixins: [goToSomewhere],
}
</script>

<style scoped>
.nav-item a {
  color: white !important;
}
</style>