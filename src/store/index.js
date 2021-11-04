import { createStore } from "vuex";



export default createStore({
  state: {
    user:{id:324234,hex:'sadssdf',active:1},
    users:[],
  },
  mutations: {
    addUser (state, user) {
      console.log(user);
      state.users.push(user);
      console.log(state.users);
    }
  },
  actions: {
    actionAddUser({commit}, value) {
      commit('addUser', value);
    },
  },
  modules: {

  },
  getters:{

  }
});
