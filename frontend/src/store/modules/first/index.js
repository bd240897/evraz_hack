import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {
            firstData: {},
        }
    },
    getters: {},
    mutations: {
        SET_FIRST_DATA(state, data) {
            state.firstData = data
        },
    },
    actions: {
        GET_FIRST_DATA({commit, rootState}, {url = this.state.FIRST_SCREEN_URL,}) {
            /**
             Получает данные для первой страницы
             */
            axios.get(url)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_FIRST_DATA', x.data)
                })
                .catch(err => {
                    console.log(err)
                    if (err.response) {
                        console.log("client received an error response (5xx, 4xx)")
                    } else if (err.request) {
                        console.log("client never received a response, or request never left")
                    } else {
                        console.log("anything else ")
                    }
                    return err
                })
        },
    },
})

