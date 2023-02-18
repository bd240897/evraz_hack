import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {
            thirdData: {},
        }
    },
    getters: {},
    mutations: {
        SET_THIRD_DATA(state, data) {
            state.thirdData = data
        },
    },
    actions: {
        GET_THIRD_DATA({commit, rootState}, {url = this.state.THIRD_SCREEN_URL}) {
            /**
             Получает данные для первой страницы
             */

            axios.get(url) //  {params: {id: id}}
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_THIRD_DATA', x.data[0]) // TODO [0] только для json-server
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

