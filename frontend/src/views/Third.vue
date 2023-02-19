<template>
  <Navbar/>

  <h1 class="screen-name text-center">Третий экран</h1>

  <!--  {{this.$route.params.id}}-->

  <section class="exausters">
    <div class="container">
      <div class="row">
        <!--Эксгаустер-->
        <div class="exauster">

          <!--          <select v-model="selected_exauster">-->
          <!--            <option v-for="option in selectData.options_exauster" v-bind:value="option.value">-->
          <!--              {{ option.text }}-->
          <!--            </option>-->
          <!--          </select>-->
          <!--          <select v-model="selected_bearing">-->
          <!--            <option v-for="option in selectData.options_bearing" v-bind:value="option.value">-->
          <!--              {{ option.text }}-->
          <!--            </option>-->
          <!--          </select>-->
          <!--          <select v-model="selected_feature">-->
          <!--            <option v-for="option in selectData.options_feature" v-bind:value="option.value">-->
          <!--              {{ option.text }}-->
          <!--            </option>-->
          <!--          </select>-->

          <!--          <span>Выбрано: {{ selected }}</span>-->


        </div>
      </div>
    </div>
  </section>

  <section class="graph">
    <div class="container">
      <h3>Mocked graphic</h3>
      <LineChart :chartData="chartData"/>
    </div>
  </section>


  <!--  &lt;!&ndash;TODO delete &ndash;&gt;-->
  <!--  <div class="open-wallet d-flex justify-content-center mb-3">-->
  <!--    <button v-on:click="setFirstData" class="button_item btn btn-primary py-3 p" type="submit">FirstData</button>-->
  <!--    <button v-on:click="setSecondData" class="button_item btn btn-primary py-3 p" type="submit">SecondData</button>-->
  <!--  </div>-->

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
        labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        datasets: [
          {
            label: 'Temperature of 1 bearing',
            backgroundColor: '#FC2525',
            data: [40.900001525878906, 39.900001525878906, 39.600001525878906, 37.900001525878906, 38.900001525878906,
              38.700001525878906, 38.700001525878906, 39.600001525878906, 39.900001525878906, 40.900001525878906,
              40.900001525878906, 39.900001525878906, 39.600001525878906, 37.900001525878906, 38.900001525878906,
              40.600001525878906, 40.900001525878906, 40.300001525878906, 39.900001525878906, 38.900001525878906,
            ]
          },
        ]
      },

      // форма выбора
      selectData: {
        options_exauster: [
          {text: 1, value: 1},
        ],
        options_bearing: [
          {text: 1, value: 1},
          {text: 2, value: 2},
          {text: 3, value: 3},
          {text: 4, value: 4},
          {text: 5, value: 5},
          {text: 6, value: 6},
          {text: 7, value: 7},
          {text: 8, value: 8},
          {text: 9, value: 9},
        ],
        options_feature: [
          {text: 'Temperature', value: "temperature"},
          {text: 'Vibration', value: "vibration"},
        ]
      },

      selected_exauster: 1,
      selected_bearing: 1,
      selected_feature: "temperature",
    }
  },
  watch: {
    selected_exauster: function () {
      console.log("selected ")
    },
    selected_bearing: function () {
      console.log("selected ")
      this.filterData()
    },
    selected_feature: function () {
      console.log("selected ")
    },
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
    filterData() {
      this.chartData = {
        labels: this.thirdData.data,
        datasets: [
          {
            label: "" + this.selected_exauster + this.selected_bearing + this.selected_feature,
            backgroundColor: '#253bfc',
            data: this.thirdData.bearings[parseInt(this.selected_bearing)][this.selected_feature].value
          },
        ]
      }
    },

    setFirstData() {
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
    setSecondData() {
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
    this.GET_THIRD_DATA({})
    // this.filterData()
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