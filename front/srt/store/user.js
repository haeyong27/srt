export const state = () => ({
    token: null,
});
  
export const mutations = {
    save_token(state, payload) {
        state.token = payload;
      }
};

export const actions = {
    register_user({rootState, commit }, payload) {
        const url = "http://127.0.0.1:8000/rest-auth/registration/"
        const params = {
            username: payload.username,
            email: payload.email,
            password1: payload.password1,
            password2: payload.password2,
        }
        this.$axios.$post(url, params).then(res=>{
            console.log(res)
            commit("save_token", res.token);
            this.$router.push("/profile/")
        })
    },
    login({rootState, commit }, payload) {
        const url = "http://127.0.0.1:8000/rest-auth/login/"
        const params = {
            username: payload.username,
            email: payload.email,
            password: payload.password,
        }
        this.$axios.$post(url, params).then(res=>{
            console.log(res)
            commit("save_token", res.token);
            this.$router.push("/profile/")
        })
    }
};
