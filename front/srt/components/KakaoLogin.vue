<template>
  <div id="app">
    <KakaoLogin
      api-key="91ccc0d2ad94bd19899540f73caa5f3c"
      image="kakao_account_login_btn_medium_wide"
      :on-success="onSuccess"
      :on-failure="onFailure"
    />
  </div>
</template>
 
<script>
import KakaoLogin from "vue-kakao-login";

// let onSuccess = data => {
//   console.log(data);
//   this.$store.commit("user/save_token", data.access_token);
//   this.$router.push("/u/");
// };
let onFailure = data => {
  console.log(data);
  console.log("failure");
};

export default {
  name: "App",
  components: {
    KakaoLogin
  },
  methods: {
    onSuccess(data) {
      console.log(data.access_token);
      this.$store.dispatch("user/kakao_get_JWT", {access_token: data.access_token});
      // this.$router.push("/u/");
    },
    onFailure
  }
};
</script>
 
<style>
</style>