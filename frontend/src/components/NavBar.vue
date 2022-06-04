<template>
    <v-app-bar height="40">
        <v-toolbar-title>{{$route.name}}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-switch class="mt-5" @change="darkMode"></v-switch>
    </v-app-bar>

</template>

<script>
export default {
  data() {
    return {
    }
  },
  methods: {
    darkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    }
  }
}

</script>

<style>
#navbar{
  width: 100% !important;
}
</style>