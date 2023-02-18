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