<template>
  <Navbar/>

  <section class="make_photo">
    <div class="container ">

      First


    </div>
  </section>
</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions} from "vuex";
import Navbar from "@/components/Navbar";

export default {
  name: "First",
  components: {
    Navbar
  },
  mixins: [goToSomewhere],
  data() {
    return {
      file: '',
      error_massage: '',
      imagePreview: '',
      showPreview: true,
    }
  },
  methods: {
  },
  created() {
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

html, body {
  height: 100%;
}

</style>