<template>
  <Navbar/>

  <h1 class="screen-name text-center">Первый экран</h1>

  <section class="exausters">
    <div class="container">
      <div class="row">

        <!--Эксгаустер-->
        <div class="exauster col-2"
             v-for="(item, index) in firstData.exausters">

          <!--Фото машины-->
          <h2 class="exauster__name">Exauster #{{ index + 1 }}</h2>
          <img class="exauster__img"
               src="https://www.aircontrolindustries.com/wp-content/uploads/2019/04/Compressor-60hz-2.jpg" alt=""
               v-on:click="goToSecond(index)"
          >

          <!--Статус работы-->
          <div class="exauster__parameter">
            <div v-if="item.work" class="exauster__parameter__work--yes">
              Работает
            </div>
            <div v-else class="exauster__parameter__work--no">
              Не работает
            </div>
          </div>

          <!--Подшипники-->
          <div class="exauster__body">>
            <h3 class="exauster__body__header">Все подшипники</h3>

            <div class="exauster__body__bearings"
                 v-for="(bearing, index) in item.bearings">

              <!--Параметры-->
              <div class="exauster__body__bearings__bearing">
                <div class="exauster__body__bearings__bearing__header"># {{ index }}</div>

                <!--Температура-->
                <div class="exauster__body__bearings__bearing__temperature alert"
                     v-bind:class="{'alert-warning': isWarning(bearing.temperature),
                                    'alert-danger': isAlarm(bearing.temperature)}"
                >
                  Temperature: {{ bearing.temperature }}
                </div>

                <!--Вибрация-->
                <div class="exauster__body__bearings__bearing__vibration alert"
                     v-bind:class="{'alert-warning': isWarning(bearing.vibration),
                                    'alert-danger': isAlarm(bearing.vibration)}"
                >
                  Vibrations: {{ bearing.vibration }}
                </div>
              </div>

            </div>

          </div>

        </div>
      </div>
    </div>
  </section>

  <!--TODO delete -->
  <div class="open-wallet d-flex justify-content-center mb-3">
    <button v-on:click="goToSecond(2)" class="button_item btn btn-primary py-3 p" type="submit">goToSecond</button>
  </div>

  <Footer/>
</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions, mapState} from "vuex";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

export default {
  name: "First",
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
    ...mapState('first', ['firstData',]),
  },
  methods: {
    ...mapActions('first', ["GET_FIRST_DATA",]),
    isWarning(str) {
      return str === 'warning'
    },
    isAlarm(str) {
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
    padding: 0 20px
    margin: 0

    &__name

    &__img
      height: auto
      width: 100%
      cursor: pointer

    &__body
      &__header
        font-size: 22px
        text-align: center

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

  // статус работы
  .exauster__parameter__work

  .exauster__parameter__work--yes
    background-color: yellow
    color: black

  .exauster__parameter__work--no
    background-color: black
    color: white
</style>