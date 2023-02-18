<template>
  <Line :data="data" :options="options"/>
</template>

<script>
// DataPage.vue
import {Line} from 'vue-chartjs'
import {Chart, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale} from 'chart.js'

Chart.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)


export default {
  name: 'LineChart',
  components: {Line},
  data() {
    return {
      // chartData: {
      //   labels: ['January', 'February', 'March'],
      //   datasets: [{data: [40, 20, 12]}]
      // },
      chartData: [
        {
          label: 'Data One',
          backgroundColor: '#FC2525',
          data: [40, 39, 10, 40, 39, 80, 40]
        },
        {
          label: 'Data Two',
          backgroundColor: '#05CBE1',
          data: [60, 55, 32, 10, 2, 12, 53]
        }
      ],
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  }
}

</script>