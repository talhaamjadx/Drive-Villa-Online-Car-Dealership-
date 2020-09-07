import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    question_count: 0,
    answer_count: 0,
    q_content: "",
    ad_image: [],
    connection: null,
    connection2: null,
  },
  mutations: {
    increment: (state) => {
      state.question_count++;
    },
    decrement: (state) => {
      state.question_count--;
    },
    ans_inc: (state) => {
      state.answer_count++;
    },
    ans_dec: (state) => {
      state.answer_count--;
    },
    get_connection: (state, payload) => {
      state.connection = new WebSocket(
        "ws://" + window.location.host + "/ws/channel/" + payload + "/"
      );
    },
    get_connection2: (state) => {
      state.connection2 = new WebSocket(
        "ws://" + window.location.host + "/ws/active/"
      );
    },
  },
  actions: {
    get_connection: ({ commit }, payload) => {
      commit("get_connection", payload);
    },
    get_connection2: ({ commit }) => {
      commit("get_connection2");
    },
  },
});
