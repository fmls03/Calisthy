<template>
    <v-app-bar height="40">
        <v-toolbar-title>{{$route.name}}</v-toolbar-title>
        <v-spacer></v-spacer>
        <div>
          <v-img v-if="$vuetify.theme.dark === true" max-height="20" max-width="20" src="./icons/switch_theme_dark.png" class="mr-2"></v-img>
          <v-img v-else max-height="20" max-width="20" src="./icons/switch_theme.png" class="mr-2"></v-img>
        </div>
        <v-switch class="mt-5" @change="darkMode"></v-switch>
    </v-app-bar>

</template>

<script>
export default {
  data() {
    return {
      iconPath: './icons/switch_theme.png',
    }
  },
  methods: {
    darkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      if ($vuetify.theme.dark === true){
        this.iconPath = './icons/switch_theme_dark.png'
      }
      else{
        this.iconPath = './icons/switch_theme.png'
      }

    }
  }
}

</script>

<style>
#navbar{
  width: 100% !important;
}
</style>