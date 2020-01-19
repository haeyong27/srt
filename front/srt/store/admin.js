export const state = () => ({
  posts: [{}]
});

export const mutations = {
  set_posts(state, payload) {
    state.posts = payload;
  }
};

export const actions = {
  post_list({ rootState, commit }) {
    const url = "http://127.0.0.1:8000/godyd/";
    const token = rootState.user.token;
    this.$axios.setToken(token, "JWT");
    this.$axios.$get(url).then(res => {
      console.log(res);
      commit("set_posts", res);
    });
  }
};
