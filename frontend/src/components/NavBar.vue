<template>
    <v-app-bar id="navbar" class="d-flex flex-row align-center justify-space-between" height="40">
      
      <p class="mb-0"> {{ $route.name }} </p>
      <v-switch @change="darkMode"></v-switch>
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
  width: 100%;
}
</style>