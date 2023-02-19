<template>
  <Navbar/>

  <h1 class="screen-name text-center">Второй экран</h1>

  <!--  {{this.$route.params.id}}-->

  <section class="second_screen mb-5">
    <div class="container">


      <div class="">
        <h2 class="exauster__name">Exauster #{{ secondData.id + 1 }}</h2>
      </div>

      <!--Статус работы-->
      <div class="exauster__work">
        <div v-if="secondData.work" class="block_exauster__params--well">
          Работает
        </div>
        <div v-else class="block_exauster__params--alert">
          Не работает
        </div>
      </div>


      <div class="row mt-5">
        <div class="col-1"></div>

        <div class="col-1">
          <div class="gas block_exauster">
            <p class="block_exauster__name">Газ</p>
            <p>Температура газа, °С 45</p>
            <p>Разряжение, мм. в. ст 74,3</p>
            <p>Уровень пыли, мг/м³ 15</p>
          </div>
        </div>


        <div class="col-4"></div>


        <div class="col-1">
          <div class="oil block_exauster  mt-4">
            <p class="block_exaust  er__name">Маслобак</p>
            <p>Уровень масла, % 34,3</p>
          </div>
        </div>

        <div class="col-1">
          <div class="d-flex flex-column mt-5">
            <div class="oil_input block_exauster">
              -233, °С
            </div>
          </div>
        </div>

        <div class="col-1">
          <div class="row">
            <div class="col-6">
              <div class="oil_input block_exauster">
                -233, °С
              </div>
            </div>
            <div class="col-6">
              <div class="oil_input block_exauster">
                -233, °С
              </div>
            </div>
          </div>


          <div class="freezer block_exauster d-flex justify-content-center">
            <div class="d-flex flex-column align-items-center justify-content-center">
              <p class="block_exauster__name">Охладитель</p>
              <img class="freezer__img" src="../assets/img/first/спираль.png" alt="">
            </div>
          </div>
          `
        </div>


        <div class="col-1">
          <div class="d-flex flex-column mt-5">
            <div class="oil_input block_exauster">
              -233, °С
            </div>
          </div>
        </div>

      </div>


      <div class="row">

        <div class="col-1"></div>

        <div class="col-1">
          <div class="vertical_funnel d-flex flex-column justify-content-center">
            <img src="../assets/img/first/воронка_нижняя.png" alt="">
          </div>
        </div>

        <div class="col-6"></div>

        <div class="col-1">
          <div class="oil_presure block_exauster">
            <p class="block_exauster__name"> Давление</p>
            <p class="block_exauster__params">Давление масла, кг/см² 2.5</p>
          </div>
        </div>


      </div>


      <div class="row">
        <div class="col-1">
          <div class="block_exauster">

            <p class="block_exauster__name">9 ПС</p>
            <p class="block_exauster__params"
               v-bind:class="isWarningOrAlarm(secondData.bearings[8].temperature.status)"
            >
              Т, °С {{ secondData.bearings[8].temperature.value }}
            </p>
          </div>

          <div class="block_exauster">

            <p class="block_exauster__name">8 ПС</p>

            <p class="block_exauster__params"
               v-bind:class="isWarningOrAlarm(secondData.bearings[7].temperature.status)"
            >
              Т, °С {{ secondData.bearings[7].temperature.value }}
            </p>

            <div v-if="secondData.bearings[7].vibrations" v-bind:class="isWarningOrAlarm(secondData.bearings[7].vibrations.status)">
              <p class="block_exauster__params">В, мм/с {{ secondData.bearings[7].vibrations.axial_value }}</p>
              <p class="block_exauster__params">Г, мм/с {{ secondData.bearings[7].vibrations.vertical_value }}</p>
              <p class="block_exauster__params">О, мм/с {{ secondData.bearings[7].vibrations.horizontal_value }}</p>
            </div>

          </div>
        </div>


        <div class="col-1 d-flex flex-column">
          <div class="horizontal_pipe d-flex flex-column w-100">
            <img src="../assets/img/first/картинка_1.png" alt="">
          </div>
          <div class="block_exauster mx-1">
            <p class="block_exauster__name">Заслонка</p>
            <p class="block_exauster__params">Открыта на: 50%</p>
          </div>
        </div>


        <div class="col-1">
          <div class="block_exauster">
            <p class="block_exauster__name">7 ПС</p>

            <p class="block_exauster__params"
               v-bind:class="isWarningOrAlarm(secondData.bearings[6].temperature.status)">
              Т, °С {{ secondData.bearings[6].temperature.value }}
            </p>

            <div v-bind:class="isWarningOrAlarm(secondData.bearings[6].temperature.status)">
              <p class="block_exauster__params">В, мм/с {{ secondData.bearings[6].vibrations.axial_value }}</p>
              <p class="block_exauster__params">Г, мм/с {{ secondData.bearings[6].vibrations.vertical_value }}</p>
              <p class="block_exauster__params">О, мм/с {{ secondData.bearings[6].vibrations.horizontal_value }}</p>
            </div>

          </div>
        </div>

        <div class="col-1">
          <div class="horizontal_pipe d-flex flex-column">
            <img src="../assets/img/first/картинка_2.png" alt="">
          </div>
        </div>


        <div class="col-1">
          <div class="d-flex flex-column align-content-between">
            <div class="block_exauster">
              <p class="block_exauster__name">4 ПС</p>

              <p class="block_exauster__params"
                 v-bind:class="isWarningOrAlarm(secondData.bearings[3].temperature.status)">
                Т, °С {{ secondData.bearings[3].temperature.value }}
              </p>

            </div>

            <div class="block_exauster">
              <p class="block_exauster__name">3 ПС</p>

              <p class="block_exauster__params"
                 v-bind:class="isWarningOrAlarm(secondData.bearings[2].temperature.status)">
                Т, °С {{ secondData.bearings[2].temperature.value }}
              </p>

            </div>

            <div class="block_exauster">
              <p class="block_exauster__name">6 ПС</p>

              <p class="block_exauster__params"
                 v-bind:class="isWarningOrAlarm(secondData.bearings[5].temperature.status)">
                Т, °С {{ secondData.bearings[5].temperature.value }}
              </p>
            </div>

            <div class="block_exauster" style="">
              <p class="block_exauster__name">5 ПС</p>

              <p class="block_exauster__params"
                 v-bind:class="isWarningOrAlarm(secondData.bearings[4].temperature.status)">
                Т, °С {{ secondData.bearings[4].temperature.value }}
              </p>
            </div>
          </div>
        </div>

        <div class="col-1">
          <div class="horizontal_pipe d-flex flex-column">
            <img src="../assets/img/first/картинка_2.png" alt="">
          </div>
        </div>


        <div class="col-1 d-flex flex-column">
          <div class="pb-2 block_exauster">
            <p class="block_exauster__name">2 ПС</p>

            <p class="block_exauster__params"
               v-bind:class="isWarningOrAlarm(secondData.bearings[1].temperature.status)">
              Т, °С {{ secondData.bearings[1].temperature.value }}
            </p>

            <div v-bind:class="isWarningOrAlarm(secondData.bearings[1].temperature.status)">
              <p class="block_exauster__params">В, мм/с {{ secondData.bearings[1].vibrations.axial_value }}</p>
              <p class="block_exauster__params">Г, мм/с {{ secondData.bearings[1].vibrations.vertical_value }}</p>
              <p class="block_exauster__params">О, мм/с {{ secondData.bearings[1].vibrations.horizontal_value }}</p>
            </div>
          </div>

        </div>


        <div class="col-1 d-flex flex-column">
          <div class="horizontal_pipe d-flex flex-column">
            <img src="../assets/img/first/картинка_2.png" alt="">
          </div>

        </div>


        <div class="col-1 d-flex flex-column">
          <div class="block_exauster">
            <p class="block_exauster__name">Главный привод</p>
            <p class="block_exauster__params">Ток привода 0</p>
            <p class="block_exauster__params">Ток двигателя 0</p>
            <p class="block_exauster__params">Напряжение ротера 0</p>
            <p class="block_exauster__params">Напряжение статера 0</p>
          </div>

          <div class="horizontal_pipe d-flex align-content-center justify-content-center">
            <img class="" src="../assets/img/first/Rectangle_8075.png" alt="">
          </div>

        </div>


        <div class="col-1 d-flex flex-column">
          <div class="horizontal_pipe d-flex flex-column">
            <img src="../assets/img/first/картинка_2.png" alt="">
          </div>
        </div>

        <div class="col-1 d-flex flex-column">
          <div class="block_exauster">
            <p class="block_exauster__name">1 ПС</p>

            <p class="block_exauster__params"
               v-bind:class="isWarningOrAlarm(secondData.bearings[0].temperature.status)">
              Т, °С {{ secondData.bearings[0].temperature.value }}
            </p>

            <div v-bind:class="isWarningOrAlarm(secondData.bearings[0].temperature.status)">
              <p class="block_exauster__params">В, мм/с {{ secondData.bearings[0].vibrations.axial_value }}</p>
              <p class="block_exauster__params">Г, мм/с {{ secondData.bearings[0].vibrations.vertical_value }}</p>
              <p class="block_exauster__params">О, мм/с {{ secondData.bearings[0].vibrations.horizontal_value }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-4"></div>
        <div class="col-5">
          <div class="horizontal_pipe d-flex flex-column" style="margin-right: 45px; margin-left: 45px">
            <img src="../assets/img/first/труба_с.png" alt="">
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
    isWarningOrAlarm(strData) {
      if (strData === 'warning') {
        return "block_exauster__params--warning"
      } else if (strData === 'alarm') {
        return "block_exauster__params--alert"
      }
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

.temperature_oil__block__img
  text-align: center

.temperature_oil__block__sensor
  color: red

.freezer__img
  width: 25%
  height: auto

p
  margin: 0 0


.col-1, .col-2, .col-3, .col-4, .col-5, .col-6
  margin: 0 0
  padding: 0 0
  font-size: 10px

.block_exauster
  background-color: #414F4F
  border-radius: 10px
  color: white
  text-align: center
  margin-bottom: 5px
  padding: 5px 5px

  &__name
    font-weight: bold
    font-size: 12px
    margin-bottom: 5px

  &__params
    margin: 2px 0

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


.exauster__work
  border-radius: 10px
  color: white
  text-align: center
  margin: 20px 0

</style>