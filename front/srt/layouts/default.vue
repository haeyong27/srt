<template>
  <v-app id="keep">
    <v-app-bar app clipped-left color="amber">
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <nuxt-link to="/u/">
        <span class="title ml-3 mr-5" to>SRT</span>
      </nuxt-link>
      <v-spacer />
      <v-spacer />
      <v-spacer />
      
      <!-- <v-btn to="/" v-if="!login">
        <v-icon>person_add</v-icon>로그인/회원가입
      </v-btn>
      <v-btn v-else @click="logout">
        로그아웃
      </v-btn> -->

      <!-- <v-list-item to="/login/">
        <v-list-item-action>
          <v-icon>person_add</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>로그인/회원가입</v-list-item-title>
        </v-list-item-content>
      </v-list-item>-->

      <!-- <v-text-field solo-inverted flat hide-details label="Search" prepend-inner-icon="search" /> -->

      <v-spacer />
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app clipped color="grey lighten-4">
      <v-list dense class="grey lighten-4">
        <template v-for="(item, i) in items">
          <v-row v-if="item.heading" :key="i" align="center">
            <v-col cols="6">
              <v-subheader v-if="item.heading">{{ item.heading }}</v-subheader>
            </v-col>
            <v-col cols="6" class="text-right">
              <v-btn small text>edit</v-btn>
            </v-col>
          </v-row>
          <v-divider v-else-if="item.divider" :key="i" dark class="my-4" />
          <v-list-item v-else :key="i" :to="`/${item.path}`">
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="grey--text">{{ item.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <v-container>
        <v-row justify="center" align="center">
          <v-col>
            <nuxt />
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  props: {
    source: String
  },
  data: () => ({
    drawer: null,
    items: [
      { icon: "home", text: "Home", path:"u/" },
      { icon: "add", text: "새로 신청하기", path: "new/" },
      { icon: "person", text: "신청 내역", path: "profile/" }
      // { divider: true },
      // { heading: "Labels" },
      // { icon: "add", text: "Create new label" },
      // { divider: true },
      // { icon: "archive", text: "Archive" },
      // { icon: "delete", text: "Trash" },
      // { divider: true },
      // { icon: "settings", text: "Settings" },
    ]
  }),
  computed: {
    login() {
       return this.$store.state.user.token
    }
  },
  methods: {
    logout() {
      this.$store.commit("user/logout")
      this.$router.push("/");
    }
  },
};
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none;
}

a {
  text-decoration: none;
}
</style>