<template>
  <Navbar/>

  <h1>Первый экран</h1>
  <section class="exausters">
    <div class="container">

      <div class="row">
        <div class="exauster col-6">

          <h2 class="exauster__name">Exauster #1</h2>

          <img class="exauster__img"
               src="https://www.aircontrolindustries.com/wp-content/uploads/2019/04/Compressor-60hz-2.jpg" alt="">

          <div class="exauster__body">>

            <h3 class="exauster__body__header">Все подшипники</h3>

            <div class="exauster__body__bearings"
                v-for="(bearing, name, index) in firstData">

              <div class="exauster__body__bearings__bearing">

                <div class="exauster__body__bearings__bearing__header"># {{index}}</div>


                <p class="exauster__body__bearings__bearing__temperature alert"
                   v-bind:class="{'alert-warning': isWarning(bearing.temperature)}"
                   :class="{'alert-danger': isAlarm(bearing.temperature)}"
                >
                  Temperature: {{ bearing.temperature }}</p>
                <p class="exauster__body__bearings__bearing__vibration alert"
                   v-bind:class="{'alert-danger': isWarning(bearing.temperature)}"
                   :class="{'alert-danger': isAlarm(bearing.temperature)}"
                >
                  Vibrations: {{ bearing.vibration }}
                </p>
              </div>
            </div>

          </div>

        </div>
      </div>
    </div>
  </section>
</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions, mapState} from "vuex";
import Navbar from "@/components/Navbar";

export default {
  name: "First",
  components: {
    Navbar
  },
  mixins: [goToSomewhere],
  data() {
    return {
      temp: '',
    }
  },
  computed: {
    ...mapState('first', ['firstData',]),
  },
  methods: {
    ...mapActions('first', ["GET_FIRST_DATA",]),
    isWarning(str) {
      console.log(str)
      return str === 'warning'
    },
    isAlarm(str) {
      console.log(str)
      return str === 'alarm'
    },
  },
  created() {
    this.GET_FIRST_DATA({})
  },
}
</script>

<style lang="sass" scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap')

html, body
  height: 100%

  .exauster
    padding: 0
    margin: 0

    &__name
    &__img
      height: auto
      width: 100%
    &__body
      &__header
      &__bearings
        &__bearing
          &__header
            padding: 0
            margin: 0
          &__vibration
            padding: 0
            margin: 0
          &__temperature
            padding: 0
            margin: 0

</style>