<template>
  <div>
    <v-btn to='/new/'>티켓 신청하기</v-btn>
    <br>
    <br>


    <div v-for="post in posts" :key="post.id">
      <v-card class="mx-auto" max-width="344" outlined>
        <v-list-item three-line>
          <v-list-item-content>
            <div>{{ post.date }}</div>
            <br>
            <v-list-item-title class="headline mb-1">
              {{post.dpt}}
              <v-icon>arrow_right</v-icon>
              {{post.arr}}
            </v-list-item-title>
            <p>성인 : {{ post.adult }}</p>
            <p>아이 : {{ post.child }}</p>
          </v-list-item-content>
          <v-list-item-avatar tile size="80"><v-icon>train</v-icon></v-list-item-avatar>
        </v-list-item>
        <v-card-actions>
          <v-spacer />
          <v-btn>수정하기</v-btn>
          <v-btn>예약 요청</v-btn>
        </v-card-actions>
      </v-card>
      <br>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        // { text: "id", value: "id" },
        // { text: "연락처", value: "phone" },
        { text: "출발역", value: "dpt" },
        { text: "도착역", value: "arr" },
        // { text: "어른", value: "adult" },
        // { text: "아이", value: "child" },
        { text: "출발일", value: "date" },
        // { text: "is_complete", value: "is_complete" },
        { text: "Edit", value: "edit", sortable: false }
        // { text: "Start", value: "start", sortable: false }
      ]
    };
  },

  computed: {
    posts() {
      return this.$store.state.post.posts;
    }
  },
  created() {
    this.$store.dispatch("post/post_list");
  },

  methods: {
    send_ticket(item) {
      this.$store.dispatch("post/start_ticket", item.id);
    }
  }
};
</script>
