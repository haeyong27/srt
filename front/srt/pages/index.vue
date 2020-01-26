<template>
  <v-app>
    <h2>SRT 취소표 자동 예매</h2>
    <kakao-login></kakao-login>
  </v-app>
</template>

<script>
import KakaoLogin from "../components/KakaoLogin";

export default {
  components: {
    KakaoLogin,
  }
};
</script>
