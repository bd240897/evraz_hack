<template>
  <Navbar/>

  <h1 class="screen-name text-center">Третий экран</h1>

  <!--  {{this.$route.params.id}}-->

  <section class="exausters">
    <div class="container">
      <div class="row">
        <!--Эксгаустер-->
        <div class="exauster">

          1234
        </div>
      </div>
    </div>
  </section>

  <LineChart :chartData="chartData"/>

    <!--TODO delete -->
  <div class="open-wallet d-flex justify-content-center mb-3">
    <button v-on:click="setFirstData" class="button_item btn btn-primary py-3 p" type="submit">FirstData</button>
    <button v-on:click="setSecondData" class="button_item btn btn-primary py-3 p" type="submit">SecondData</button>
  </div>

  <Footer/>
</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions, mapState} from "vuex";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import BarChart from "@/components/graphs/BarChart";
import LineChart from "@/components/graphs/LineChart";

export default {
  name: "Third",
  components: {
    Navbar,
    Footer,
    BarChart,
    LineChart
  },
  mixins: [goToSomewhere],
  data() {
    return {
      temp: '',
      chartData: {
        labels: ['January', 'February', 'March'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#FC2525',
            data: [40, 20, 12]
          },
          {
            label: 'Data Two',
            backgroundColor: '#05CBE1',
            data: [45, 20, 12]
          },
        ]
      },
    }
  },
  computed: {
    ...mapState('third', ['thirdData',]),
  },
  methods: {
    ...mapActions('third', ["GET_THIRD_DATA",]),
    isWarning(str) {
      return str === 'warning'
    },
    isAlarm(str) {
      return str === 'alarm'
    },
    setFirstData(){
      this.chartData = {
        labels: ['January', 'February', 'March'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#FC2525',
            data: [40, 20, 12]
          },
        ]
      }
    },
    setSecondData(){
      this.chartData = {
        labels: ['January', 'February', 'March'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#253bfc',
            data: [400, 200, 120]
          },
        ]
      }
    },


  },
  created() {
    this.GET_THIRD_DATA()
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