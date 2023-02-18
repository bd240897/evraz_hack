<template>
  <Line
      id="my-chart-id"
      :options="chartOptions"
      :data="chartData"
  />
</template>

<script>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'

import {Line} from 'vue-chartjs'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)

export default {
  name: 'LineChart',
  components: {Line},
  props: ["chartData"],
  data() {
    return {
      // chartData: {
      //   labels: ['January', 'February', 'March'],
      //   datasets: [
      //     {
      //       label: 'Data One',
      //       backgroundColor: '#FC2525',
      //       data: [40, 20, 12]
      //     },
      //     {
      //       label: 'Data Two',
      //       backgroundColor: '#05CBE1',
      //       data: [45, 20, 12]
      //     },
      //   ]
      // },

      chartOptions: {
        responsive: true,
      }
    }
  }
}
</script>