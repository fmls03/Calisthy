<template>
    <v-app-bar height="40">
        <v-toolbar-title>{{$route.name}}</v-toolbar-title>
        <v-spacer></v-spacer>

        <div v-if="$session.get('username') != null ">
          <v-icon class="mr-2" height="20" width="20" v-on:click="logout">mdi-logout</v-icon>
        </div>
        <div>
          <v-img v-if="$vuetify.theme.dark === true" max-height="20" max-width="20" src="./icons/switch_theme_dark.png" class="mr-2"></v-img>
          <v-img v-else max-height="20" max-width="20" src="./icons/switch_theme.png" class="mr-2"></v-img>
        </div>

        <v-switch :input-value="$vuetify.theme.dark" class="mt-5  " @change="darkMode"></v-switch>
    </v-app-bar>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
    }
  },
  methods: {
    async darkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      
      const payload = {
        username: this.$session.get('username'),
      };

      await axios.post(`/api/user/changeTheme`, payload)    

    },

    logout(){
      this.$session.clear();
      window.location.replace('/login')
    }
  }
 
}

</script>

<style>
#navbar{
  width: 100% !important;
}

</style>