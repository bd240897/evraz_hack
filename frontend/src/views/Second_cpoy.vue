<template>
  <Navbar/>

  <h1 class="screen-name text-center">Второй экран</h1>

  <!--  {{this.$route.params.id}}-->

  <section class="second_screen">
    <div class="container">









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
                        <img class="freezer__img" src="./static/img/first/спираль.png" alt="">
                    </div>
                </div>
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
                    <img src="./static/img/first/воронка нижняя.png" alt="">
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
                    <p class="block_exauster__params">Т, °С 220</p>
                </div>
                <div class="block_exauster">
                    <p class="block_exauster__name">8 ПС</p>
                    <p class="block_exauster__params">Т, °С 220</p>
                    <p class="block_exauster__params">В, мм/с 8</p>
                    <p class="block_exauster__params">Г, мм/с 00</p>
                    <p class="block_exauster__params">О, мм/с 00</p>
                </div>
            </div>


            <div class="col-1 d-flex flex-column">
                <div class="horizontal_pipe d-flex flex-column w-100">
                    <img src="./static/img/first/картинка 1.png" alt="">
                </div>
                <div class="block_exauster mx-1">
                    <p class="block_exauster__name">Заслонка</p>
                    <p class="block_exauster__params">Открыта на: 50%</p>
                </div>
            </div>


            <div class="col-1">
                <div class="block_exauster">
                    <p class="block_exauster__name">7 ПС</p>
                    <p class="block_exauster__params">Т, °С 220</p>
                    <p class="block_exauster__params">В, мм/с 8</p>
                    <p class="block_exauster__params block_exauster__params--warning">Г, мм/с 00</p>
                    <p class="block_exauster__params">О, мм/с 00</p>
                </div>
            </div>

            <div class="col-1">
                <div class="horizontal_pipe d-flex flex-column">
                    <img src="./static/img/first/картинка 2.png" alt="">
                </div>
            </div>


            <div class="col-1">
                <div class="d-flex flex-column align-content-between">
                    <div class="block_exauster">
                        <p class="block_exauster__name">4 ПС</p>
                        <p class="block_exauster__params">Т, °С 220</p>
                    </div>

                    <div class="block_exauster">
                        <p class="block_exauster__name">3 ПС</p>
                        <p class="block_exauster__params">Т, °С 220</p>
                    </div>

                    <div class="block_exauster">
                        <p class="block_exauster__name">6 ПС</p>
                        <p class="block_exauster__params">Т, °С 220</p>
                    </div>

                    <div class="block_exauster" style="">
                        <p class="block_exauster__name">5 ПС</p>
                        <p class="block_exauster__params">Т, °С 220</p>
                    </div>
                </div>
            </div>

            <div class="col-1">
                <div class="horizontal_pipe d-flex flex-column">
                    <img src="./static/img/first/картинка 2.png" alt="">
                </div>
            </div>


            <div class="col-1 d-flex flex-column">
                <div class="pb-2 block_exauster">
                    <p class="block_exauster__name">2 ПС</p>
                    <p class="block_exauster__params block_exauster__params--alert">Т, °С 220</p>
                    <p class="block_exauster__params">В, мм/с 8</p>
                    <p class="block_exauster__params">Г, мм/с 00</p>
                    <p class="block_exauster__params">О, мм/с 00</p>
                </div>

            </div>


            <div class="col-1 d-flex flex-column">
                <div class="horizontal_pipe d-flex flex-column">
                    <img src="./static/img/first/картинка 2.png" alt="">
                </div>

            </div>


            <div class="col-1 d-flex flex-column">
                <div class="block_exauster">
                    <p class="block_exauster__name">Главный привод</p>
                    <p class="block_exauster__params">Ток, А Главный привод 000</p>
                    <p class="block_exauster__params">Ток двигателя, А 000</p>
                    <p class="block_exauster__params">Напряжение ротера, кВт 000</p>
                    <p class="block_exauster__params">Напряжение статера, кВт 000</p>
                </div>

                <div class="horizontal_pipe d-flex align-content-center justify-content-center">
                    <img class="" src="./static/img/first/Rectangle%208075.png" alt="">
                </div>

            </div>


            <div class="col-1 d-flex flex-column">
                <div class="horizontal_pipe d-flex flex-column">
                    <img src="./static/img/first/картинка 2.png" alt="">
                </div>
            </div>

            <div class="col-1 d-flex flex-column">
                <div class="block_exauster">
                    <p class="block_exauster__name">1 ПС</p>
                    <p class="block_exauster__params">Т, °С 220</p>
                    <p class="block_exauster__params">В, мм/с 8</p>
                    <p class="block_exauster__params">Г, мм/с 00</p>
                    <p class="block_exauster__params">О, мм/с 00</p>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-4"></div>
            <div class="col-5">
                <div class="horizontal_pipe d-flex flex-column" style="margin-right: 45px; margin-left: 45px">
                    <img src="./static/img/first/труба%20с.png" alt="">
                </div>
            </div>
        </div>
    </div>
</section>



  <section class="exausters">
    <div class="container">
      <div class="row">
        <!--Эксгаустер-->
        <div class="exauster">

<!--          &lt;!&ndash;TODO delete &ndash;&gt;-->
<!--          <div class="open-wallet d-flex justify-content-center mb-3">-->
<!--            <button v-on:click="goToFirst" class="button_item btn btn-primary py-3 p" type="submit">-->
<!--              goToFirst-->
<!--            </button>-->
<!--          </div>-->

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