import { createStore } from "vuex";



export default createStore({
  state: {
    user:{id:324234,hex:'sadssdf',active:1},
    users:[],

  },
  mutations: {
    addUser (state, user) {
      state.users.push(user)
    }

  },
  actions: {

  },
  modules: {

  },
  getters:{

  }
});
