import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {
            secondData: {},
        }
    },
    getters: {},
    mutations: {
        SET_SECOND_DATA(state, data) {
            state.secondData = data
        },
    },
    actions: {
        GET_SECOND_DATA({commit, rootState}, {id, url = this.state.SECOND_SCREEN_URL,}) {
            /**
             Получает данные для первой страницы
             */
            console.log(id)
            axios.get(url, {params: {id: id}})
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_SECOND_DATA', x.data[0]) // TODO [0] только для json-server
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

