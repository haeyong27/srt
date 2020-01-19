<template>
  <div>
    <h1>login</h1>
    <v-form v-on:submit.prevent="submit">
      <v-text-field v-model="username" label="username"></v-text-field>
      <v-text-field v-model="email" label="email"></v-text-field>
      <v-text-field v-model="password" label="password"></v-text-field>
      <button>로그인하기</button>
      <nuxt-link to="/register/">회원가입하기</nuxt-link>
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
