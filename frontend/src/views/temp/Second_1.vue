<template>
  <Navbar/>

  <h1 class="screen-name text-center">Второй экран</h1>

  {{this.$route.params.id}}

  <section class="exausters">
    <div class="container">
      <div class="row">
        <!--Эксгаустер-->
        <div class="exauster col-2"
             v-for="(item, index) in secondData.exausters">


          <h2 class="exauster__name">Exauster #{{ index + 1 }}</h2>
          <img class="exauster__img"
               src="https://www.aircontrolindustries.com/wp-content/uploads/2019/04/Compressor-60hz-2.jpg" alt="">

          <!--Подшипники-->
          <div class="exauster__body">>
            <h3 class="exauster__body__header">Все подшипники</h3>

            <div class="exauster__body__bearings"
                 v-for="(bearing, index) in item.bearings">

              <!--Параметры-->
              <div class="exauster__body__bearings__bearing">
                <div class="exauster__body__bearings__bearing__header"># {{ index }}</div>

                <div class="exauster__body__bearings__bearing__temperature alert"
                     v-bind:class="{'alert-warning': isWarning(bearing.temperature.status)}"
                     :class="{'alert-danger': isAlarm(bearing.temperature.status)}"
                >
                  <p>Temperature: {{ bearing.temperature.value }}</p>
                  <p>Status: {{ bearing.temperature.status }}</p>
                </div>

                <div class="exauster__body__bearings__bearing__vibration alert"
                     v-if="bearing.vibrations"
                     v-bind:class="{'alert-danger': isWarning(bearing.vibrations.status)}"
                     :class="{'alert-danger': isAlarm(bearing.vibrations.status)}"
                >
                  <p>Vibrations A: {{ bearing.vibrations.axial_value }}</p>
                  <p>Vibrations V: {{ bearing.vibrations.vertical_value }}</p>
                  <p>ibrations H: {{ bearing.vibrations.horizontal_value }}</p>
                  <p>Status: {{ bearing.vibrations.status }}</p>
                </div>
              </div>

            </div>

          </div>

        </div>
      </div>
    </div>
  </section>

  <Footer/>
</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions, mapState} from "vuex";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

export default {
  name: "Second",
  components: {
    Navbar,
    Footer
  },
  mixins: [goToSomewhere],
  data() {
    return {
      temp: '',
    }
  },
  computed: {
    ...mapState('second', ['secondData',]),
  },
  methods: {
    ...mapActions('second', ["GET_SECOND_DATA",]),
    isWarning(str) {
      return str === 'warning'
    },
    isAlarm(str) {
      return str === 'alarm'
    },
  },
  created() {
    this.GET_SECOND_DATA({id: this.$route.params.id})
  },
}
</script>

<style lang="sass" scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap')

html, body
  height: 100%

  .exauster
    padding: 0 20px
    margin: 0

    &__name
      font-weight: bold

    &__img
      height: auto
      width: 100%

    &__body
      &__header
        font-size: 22px
        text-align: center

      &__bearings
        &__bearing
          &__header
            padding: 0
            margin: 0
            font-weight: bold

          &__vibration
            padding: 0
            margin: 0

            p
              padding: 0
              margin: 0

          &__temperature
            padding: 0
            margin: 0

            p
              padding: 0
              margin: 0

</style>