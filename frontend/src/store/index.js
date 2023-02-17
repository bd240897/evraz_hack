import { createStore } from 'vuex'
import first from "./modules/first/";


export default createStore({
  state() {
    return {
      // TODO
      BASE_URL: " http://localhost:3004", // process.env.VUE_APP_API_URL || "http://127.0.0.1:8000", // 'http://84.201.135.220:8000', //'http://127.0.0.1:8000',
      FIRST_SCREEN_URL: "/get-first-screen/",
    }
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    first,
  }
})
