<template>
  <Navbar/>

  <h1 class="screen-name text-center">Первый экран</h1>

  <section class="first_screen">
    <div class="container">
      <div class="row">


        <div class="col-4 block_machines mx-0 px-0 ">

          <h2 class="block_machines__name mx-0 px-0 py-2">Агломашина №1</h2>

          <div class="container mx-0 px-0">
            <div class="row mx-0 px-0 pb-3">

              <div class="col-6 p-3"
                   v-for="(item, index) in [firstData.exausters[0],firstData.exausters[1]]"
              >
                <div class="block_machines__exauster m-1 p-1 rounded-2">
                  <h3 class="block_machines__exauster__name py-2">Эксгаустер №{{ item.id }}</h3>
                  <div class="">
                    <img class="block_machines__exauster__img"
                         src="../assets/img/second/эксгаустер_1.png" alt=""
                         v-on:click="goToSecond(item.id)">
                  </div>

                  <div class="bearings container-fluid  pb-3">
                    <div class="row">
                      <h5 class="working__name">Статус</h5>

                      <!--Статус работы-->
                      <div v-if="item.work" class="working__status working__status--work">Работает</div>
                      <div v-else class="working__status working__status--nowork">Работает</div>

                    </div>

                    <h5 class="bearings__name">Все подшипники</h5>
                    <div v-for="(bearing, index) in item.bearings" class="row bearings__parameters">

                      <div class="bearings__parameters__number col-3 text-center mx-1">
                        #{{ bearing.id }}
                      </div>

                      <div class="bearings__parameters__number col-3 text-center mx-1"
                      v-bind:class="isWarningOrAlarm(bearing.temperature)"
                      >
                        T
                      </div>

                      <div v-if="bearing.vibration" class="bearings__parameters__number col-3 text-center mx-1"
                      v-bind:class="isWarningOrAlarm(bearing.vibration)"
                      >
                        V
                      </div>

                    </div>

                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <div class="col-4 block_machines mx-0 px-0 ">

          <h2 class="block_machines__name mx-0 px-0 py-2">Агломашина №2</h2>

          <div class="container mx-0 px-0">
            <div class="row mx-0 px-0 pb-3">

              <div class="col-6 p-3"
                   v-for="(item, index) in [firstData.exausters[2],firstData.exausters[3]]"
              >
                <div class="block_machines__exauster m-1 p-1 rounded-2">
                  <h3 class="block_machines__exauster__name py-2">Эксгаустер №{{ item.id }}</h3>
                  <div class="">
                    <img class="block_machines__exauster__img"
                         src="../assets/img/second/эксгаустер_1.png" alt=""
                         v-on:click="goToSecond(item.id)">
                  </div>

                  <div class="bearings container-fluid  pb-3">
                    <div class="row">
                      <h5 class="working__name">Статус</h5>

                      <!--Статус работы-->
                      <div v-if="item.work" class="working__status working__status--work">Работает</div>
                      <div v-else class="working__status working__status--nowork">Работает</div>

                    </div>

                    <h5 class="bearings__name">Все подшипники</h5>
                    <div v-for="(bearing, index) in item.bearings" class="row bearings__parameters">

                      <div class="bearings__parameters__number col-3 text-center mx-1">
                        #{{ bearing.id }}
                      </div>

                      <div class="bearings__parameters__number col-3 text-center mx-1"
                      v-bind:class="isWarningOrAlarm(bearing.temperature)"
                      >
                        T
                      </div>

                      <div v-if="bearing.vibration" class="bearings__parameters__number col-3 text-center mx-1"
                      v-bind:class="isWarningOrAlarm(bearing.vibration)"
                      >
                        V
                      </div>

                    </div>

                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <div class="col-4 block_machines mx-0 px-0 ">

          <h2 class="block_machines__name mx-0 px-0 py-2">Агломашина №2</h2>

          <div class="container mx-0 px-0">
            <div class="row mx-0 px-0 pb-3">

              <div class="col-6 p-3"
                   v-for="(item, index) in [firstData.exausters[4],firstData.exausters[5]]"
              >
                <div class="block_machines__exauster m-1 p-1 rounded-2">
                  <h3 class="block_machines__exauster__name py-2">Эксгаустер №{{ item.id }}</h3>
                  <div class="">
                    <img class="block_machines__exauster__img"
                         src="../assets/img/second/эксгаустер_1.png" alt=""
                         v-on:click="goToSecond(item.id)">
                  </div>

                  <div class="bearings container-fluid  pb-3">
                    <div class="row">
                      <h5 class="working__name">Статус</h5>

                      <!--Статус работы-->
                      <div v-if="item.work" class="working__status working__status--work">Работает</div>
                      <div v-else class="working__status working__status--nowork">Работает</div>

                    </div>

                    <h5 class="bearings__name">Все подшипники</h5>
                    <div v-for="(bearing, index) in item.bearings" class="row bearings__parameters">

                      <div class="bearings__parameters__number col-3 text-center mx-1">
                        #{{ bearing.id }}
                      </div>

                      <div class="bearings__parameters__number col-3 text-center mx-1"
                      v-bind:class="isWarningOrAlarm(bearing.temperature)"
                      >
                        T
                      </div>

                      <div v-if="bearing.vibration" class="bearings__parameters__number col-3 text-center mx-1"
                      v-bind:class="isWarningOrAlarm(bearing.vibration)"
                      >
                        V
                      </div>

                    </div>

                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

      </div>
    </div>
  </section>


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
    isWarningOrAlarm(strData) {
      if (strData === 'warning') {
        return "block_exauster__params--warning"
      } else if (strData === 'alarm') {
        return "block_exauster__params--alert"
      }
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


.block_machines
  background-color: #6c757d
  border-radius: 2px
  color: white
  text-align: center

  &__exauster
    background-color: white
    border-radius: 2px
    border-color: black
    color: black


    &__img
      width: auto
      height: auto
      max-height: 100%
      max-width: 100%
      cursor: pointer

.bearings

  .working__status
    border-radius: 1px
    border: solid #77787f

    &--work
      background-color: green

    &--nowork
      background-color: red

  &__parameters
    margin-bottom: 10px

    &__number
      border-radius: 5px
      border: solid #77787f
      background-color: #d7d8da


.block_exauster__params

    &--alert
      background-color: red
      font-weight: bold
      border-radius: 5px

    &--warning
      background-color: #ffc107
      font-weight: bold
      border-radius: 5px

    &--well
      background-color: green
      font-weight: bold
      border-radius: 5px

</style>