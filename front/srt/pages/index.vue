<template>
  <v-data-table :headers="headers" :items="posts" sort-by="calories" class="elevation-1">
    <template v-slot:item.action="{ item }">
      <v-icon small class="mr-2" @click="send_ticket(item)">edit</v-icon>
    </template>
  </v-data-table>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        { text: "id", value: "id" },
        { text: "연락처", value: "phone" },
        { text: "출발역", value: "dpt" },
        { text: "도착역", value: "arr" },
        { text: "어른", value: "adult" },
        { text: "아이", value: "child" },
        { text: "출발일", value: "date" },
        { text: "is_complete", value: "is_complete" },
        { text: "Actions", value: "action", sortable: false }
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
