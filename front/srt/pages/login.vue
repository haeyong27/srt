<template>
  <div>
    <h1>login</h1>
    <v-form v-on:submit.prevent="submit">
      <v-text-field v-model="username" label="username"></v-text-field>
      <v-text-field v-model="email" label="email"></v-text-field>
      <v-text-field v-model="password" label="password"></v-text-field>
      <v-btn @click="submit">로그인</v-btn>
      <v-btn to="/register/">회원가입</v-btn>
    </v-form>

  </div>
</template>

<script>
export default {
  data() {
    return {
        username: 'ghkdgodydzz',
        email: 'ghkdgodydzz@gmail.com',
        password: 'ghkdgodydzz',
    };
  },
  methods: {
    submit() {
      this.$store.dispatch("user/login", {
        username: this.username,
        email: this.email,
        password: this.password,
      });
    }
  }
};
</script>
