<template>
  <div>
    <h1>내 정보</h1>
    <br>
    <p>SRT ID : </p>
    <p>SRT 비밀번호 : </p>

    <h2>신청내역</h2>
    <!-- <v-data-table :headers="headers" :items="posts" :items-per-page="10" class="elevation-1"></v-data-table> -->
    {{posts}}

  </div>
</template>

<script>
export default {
    data () {
      return {
        headers: [
          { text: '출발역', value: 'station_depart'},
          { text: '도착역', value: 'station_arrive'},
          { text: '어른', value: 'num_adult'},
          { text: '아이', value: 'num_child'},
          { text: '출발일', value: 'date'},
        ],
      }
    },

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
