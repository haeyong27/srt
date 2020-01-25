<template>
  <div>
    <!-- <button @click="handleClickGetAuth" :disabled="!isInit">
      <v-btn>
        구글로 로그인하기
      </v-btn>
    </button> -->
    <v-btn @click="handleClickSignIn" :disabled="!isInit">구글로 로그인 하기</v-btn>
    <!-- <v-btn @click="handleClickSignIn" v-if="!isSignIn" :disabled="!isInit">구글로 로그인 하기</v-btn> -->
    <!-- <v-btn @click="handleClickSignOut" v-if="isSignIn" :disabled="!isInit">구글로 로그인 하기</v-btn> -->
  </div>
</template>

<script>
import Vue from 'vue'
import GAuth from 'vue-google-oauth2'

const gauthOption = {
    clientId: '1017718574091-pm9lsnsv17geo4dfdam87j6lgis4ga9m.apps.googleusercontent.com',
    scope: 'profile email',
    prompt: 'select_account'
  }

Vue.use(GAuth, gauthOption)


export default {
  name: 'test',
  data () {
    return {
      isInit: false,
      isSignIn: false
    }
  },

  methods: {
    handleClickGetAuth(){
      this.$gAuth.getAuthCode()
      .then(authCode => {
        return this.$axios.post('http://127.0.0.1:8000/accounts/rest-auth/google/', { code: authCode, redirect_uri : 'http://127.0.0.1:8000/accounts/google/login/callback/'})
      })
      .then(res => {
        // 토큰 장고에서 받아온거 저장하기 
        console.log(res)
        this.$store.commit('user/set_token', res.data.token)
        this.$store.commit('user/set_authenticated')
      })
      .catch(error => {
        console.log(error)
      })

    },

    handleClickSignIn(){
      this.$gAuth.signIn()
      .then(user => {
        // On success do something, refer to https://developers.google.com/api-client-library/javascript/reference/referencedocs#googleusergetid
        console.log('user', user)
      })
      .catch(error  => {
        // On fail do something
      })
    },

    handleClickSignOut(){
      this.$gAuth.signOut()
      .then(() => {
        // On success do something
        this.isSignIn = this.$gAuth.isAuthorized
      })
      .catch(error  => {
        // On fail do something
      })
    }
  },
  mounted(){
    let that = this
    let checkGauthLoad = setInterval(function(){
      that.isInit = that.$gAuth.isInit
      that.isSignIn = that.$gAuth.isAuthorized
      if(that.isInit) clearInterval(checkGauthLoad)
    });
  }
  
}
</script>