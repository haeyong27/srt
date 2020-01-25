<template>
  <!-- <v-form v-on:submit.prevent="submit">
      <v-text-field v-model="username" label="username"></v-text-field>
      <v-text-field v-model="email" label="email"></v-text-field>
      <v-text-field v-model="password" label="password"></v-text-field>
      <v-btn @click="submit">로그인</v-btn>
      <v-btn to="/register/">회원가입</v-btn>
  </v-form>-->
  <v-app>
    <h2>SRT 취소표 자동 예매</h2>
    <br>
    <kakao-login></kakao-login>
    <!-- <v-btn to="/new/">회원가입하지 않고 예매하기</v-btn> -->
  </v-app>
</template>

<script>
import KakaoLogin from "../components/KakaoLogin";
// import GoogleLogin from "../components/GoogleLogin";
// import FacebookLogin from "../components/FacebookLogin";

export default {
  // data() {
  //   return {
  //     username: "ghkdgodydzz",
  //     email: "ghkdgodydzz@gmail.com",
  //     password: "ghkdgodydzz"
  //   };
  // },
  methods: {
    // submit() {
    //   this.$store.dispatch("user/login", {
    //     username: this.username,
    //     email: this.email,
    //     password: this.password
    //   });
    // },
    // get_access() {
    //   this.$store.dispatch("user/get_access");
    // }
  },
  components: {
    // GoogleLogin,
    KakaoLogin,
    // FacebookLogin,
  }
};
</script>
