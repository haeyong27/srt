<template>
  <div>
    <h1>register</h1>
    <v-form v-on:submit.prevent="submit">
      <v-text-field v-model="username" label="username"></v-text-field>
      <v-text-field v-model="email" label="email"></v-text-field>
      <v-text-field v-model="password1" label="password1"></v-text-field>
      <v-text-field v-model="password2" label="password2"></v-text-field>
      <button>등록하기</button>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
        username: 'ghkdgodydzz',
        email: 'ghkdgodydzz@gmail.com',
        password1: 'ghkdgodydzz',
        password2: 'ghkdgodydzz',
    };
  },
  methods: {
    submit() {
      this.$store.dispatch("user/register_user", {
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,
      });
    }
  }
};
</script>
