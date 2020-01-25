<template>
    <div>
        <client-only>
            <v-facebook-login app-id="966242223397117"></v-facebook-login>
        </client-only>
    </div>
</template>
<script>
import VFacebookLogin from 'vue-facebook-login-component'

export default {
    components: {
      VFacebookLogin
    }
  }
</script>