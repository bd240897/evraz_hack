<template>
  <Navbar/>

  <h1 class="screen-name text-center">Первый экран</h1>

  <section class="exausters">
    <div class="container">
      <div class="row">
123123
<!--        &lt;!&ndash;Эксгаустер&ndash;&gt;-->
<!--        <div class="exauster col-2"-->
<!--             v-for="(item, index) in firstData">-->

<!--          <h2 class="exauster__name">Exauster #{{ index + 1 }}</h2>-->
<!--          <img class="exauster__img"-->
<!--               src="https://www.aircontrolindustries.com/wp-content/uploads/2019/04/Compressor-60hz-2.jpg" alt="">-->

<!--          &lt;!&ndash;Подшипники&ndash;&gt;-->
<!--          <div class="exauster__body">>-->
<!--            <h3 class="exauster__body__header">Все подшипники</h3>-->

<!--            <div class="exauster__body__bearings"-->
<!--                 v-for="(bearing, name, index) in item.exauster">-->

<!--               &lt;!&ndash;Параметры&ndash;&gt;-->
<!--              <div class="exauster__body__bearings__bearing">-->
<!--                <div class="exauster__body__bearings__bearing__header"># {{ index }}</div>-->
<!--                <p class="exauster__body__bearings__bearing__temperature alert"-->
<!--                   v-bind:class="{'alert-warning': isWarning(bearing.temperature)}"-->
<!--                   :class="{'alert-danger': isAlarm(bearing.temperature)}"-->
<!--                >-->
<!--                  Temperature: {{ bearing.temperature }}</p>-->
<!--                <p class="exauster__body__bearings__bearing__vibration alert"-->
<!--                   v-bind:class="{'alert-danger': isWarning(bearing.temperature)}"-->
<!--                   :class="{'alert-danger': isAlarm(bearing.temperature)}"-->
<!--                >-->
<!--                  Vibrations: {{ bearing.vibration }}-->
<!--                </p>-->
<!--              </div>-->

<!--            </div>-->

<!--          </div>-->

<!--        </div>-->
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
    this.GET_SECOND_DATA({})
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

</style>