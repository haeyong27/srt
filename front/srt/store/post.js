export const state = () => ({
  posts: [{
    id: null,
    station_depart: "",
    station_arrive: "",
    num_adult: "",
    num_child: "",
    date: "",
    time_begin: "",
    time_end: "",
    status: "",
    user: null,
  }]
});

export const mutations = {
  set_posts(state, payload) {
    state.posts = payload;
  }
};

export const actions = {
  register_post({ rootState }, payload) {
    const url = "http://127.0.0.1:8000/post/";
    const token = rootState.user.token;
    const params = {
      station_depart: payload.station_depart,
      station_arrive: payload.station_arrive,
      num_adult: payload.num_adult,
      num_child: payload.num_child,
      date: payload.date,
      time_begin: payload.time_begin,
      time_end: payload.time_end
    };
    this.$axios.setToken(token, "bearer");
    this.$axios.$post(url, params).then(res => {
      console.log(res);
      this.$router.push("/");
    });
  },

  register_ticket({ rootState }, payload) {
    const url = "http://127.0.0.1:8000/ticket/";
    const params = {
      srtid: payload.srtid,
      srtpw: payload.srtpw,
      logintype: payload.logintype,
      dpt: payload.dpt,
      arr: payload.arr,
      adult: payload.adult,
      child: payload.child,
      date: payload.date,
      dptime: payload.dptime,
      ticketnum: payload.ticketnum,
      phone: payload.phone,
    };
    this.$axios.$post(url, params).then(res => {
      console.log(res);
      this.$router.push("/u/");
    });
  },

  start_ticket({rootState}, payload) {
    const url = "http://127.0.0.1:8000/ticketing/"+payload;
    // const token = rootState.user.token;
    // this.$axios.setToken(token, "bearer");
    console.log(payload)
    this.$axios.$get(url)
  },

  

  post_list({ rootState, commit }) {
    const url = "http://127.0.0.1:8000/ticket/";
    const token = rootState.user.token;
    // this.$axios.setToken(token, "bearer");
    this.$axios.$get(url).then(res => {
      console.log(res);
      commit("set_posts", res);
    });
  }
};
