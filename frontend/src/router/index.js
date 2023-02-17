import {createRouter, createWebHistory} from 'vue-router'
import MainView from '../views/MainView.vue'
import First from '../views/First.vue'



const routes = [
    {
        path: '/',
        name: 'MainView',
        component: MainView
    },
    {
        path: '/first-screen',
        name: 'First',
        component: First
    },
]

const router = createRouter({
    history: createWebHistory(), //process.env.BASE_URL
    routes
})

export default router
