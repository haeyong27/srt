<template>
  <div>
    <h1>내 정보</h1>
    <br>
    <p>SRT ID : </p>
    <p>SRT 비밀번호 : </p>

    <h2>신청내역</h2>
    {{ posts }}
  </div>
</template>

<script>
export default {
  computed: {
    posts() {
      return this.$store.state.post.posts;
    }
  },
  created() {
    this.$store.dispatch("post/post_list");
  }
};
</script>
