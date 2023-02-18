<template>
  <Navbar/>

  <h1 class="screen-name text-center">Второй экран</h1>

  <!--  {{this.$route.params.id}}-->

  <section class="exausters">
    <div class="container">
      <div class="row">
        <!--Эксгаустер-->
        <div class="exauster">

          <!--TODO delete -->
          <div class="open-wallet d-flex justify-content-center mb-3">
            <button v-on:click="goToFirst" class="button_item btn btn-primary py-3 p" type="submit">
              goToFirst
            </button>
          </div>

          <!--Фото машины-->
          <div class="col-6">
            <h2 class="exauster__name">Exauster #{{ secondData.id + 1 }}</h2>
            <img class="exauster__img"
                 src="https://www.aircontrolindustries.com/wp-content/uploads/2019/04/Compressor-60hz-2.jpg" alt="">
          </div>

          <div class="exauster__body row mb-2">>

            <h3 class="exauster__body__header">Все подшипники</h3>

            <!--Статус работы-->
            <div class="exauster__parameter">
              <div v-if="secondData.work" class="exauster__parameter__work--yes">
                Работает
              </div>
              <div v-else class="exauster__parameter__work--no">
                Не работает
              </div>
            </div>

            <!--Подшипники-->
            <div class="exauster__body__bearings border border-primary col-3"
                 v-for="(bearing, index) in secondData.bearings">

              <!--Параметры-->
              <div class="exauster__body__bearings__bearing">
                <div class="exauster__body__bearings__bearing__header"># {{ index }}</div>


                <!--Температура-->
                <div class="exauster__body__bearings__bearing__temperature alert"
                     v-bind:class="{'alert-warning': isWarning(bearing.temperature.status),
                                    'alert-danger': isAlarm(bearing.temperature.status)}"
                >
                  <p>Temperature: {{ bearing.temperature.value }}</p>
                  <p>Status: {{ bearing.temperature.status }}</p>
                </div>

                <!--Вибрация-->
                <div class="exauster__body__bearings__bearing__vibration alert"
                     v-if="bearing.vibrations"
                     v-bind:class="{'alert-warning': isWarning(bearing.vibrations.status),
                                    'alert-danger': isAlarm(bearing.vibrations.status)}"
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


  // статус работы
  .exauster__parameter__work

  .exauster__parameter__work--yes
    background-color: yellow
    color: black

  .exauster__parameter__work--no
    background-color: black
    color: white
</style>