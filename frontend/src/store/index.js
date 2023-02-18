import { createStore } from 'vuex'
import first from "./modules/first/";
import second from "./modules/second/";
import third from "./modules/third/";

export default createStore({
  state() {
    return {
      // TODO
      BASE_URL: process.env.VUE_APP_API_URL || "http://localhost:3004", // 'http://84.201.135.220:8000', //'http://127.0.0.1:8000',
      FIRST_SCREEN_URL: "/get-first-screen/",
      SECOND_SCREEN_URL: "/get-second-screen/",
      THIRD_SCREEN_URL: "/get-third-screen/",

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
    second,
    third
  }
})
