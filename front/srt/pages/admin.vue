<template>
  <div>
    <h1>관리 페이지</h1>

    <h2>신청내역</h2>
    <v-data-table :headers="headers" :items="posts" :items-per-page="50" class="elevation-1"></v-data-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        { text: "출발역", value: "station_depart" },
        { text: "도착역", value: "station_arrive" },
        { text: "어른", value: "num_adult" },
        { text: "아이", value: "num_child" },
        { text: "출발일", value: "date" }
      ]
    };
  },

  computed: {
    posts() {
      return this.$store.state.admin.posts;
    }
  },
  created() {
    this.$store.dispatch("admin/post_list");
  }
};
</script>
