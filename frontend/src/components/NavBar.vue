<template>
    <div>
        <v-app-bar height="40">
            {{ $route.name }}
            
        </v-app-bar>
    </div>

</template>

<script>
export default {
  name: 'App',
  data: () => ({ 
      darkMode: false
    }),
    methods: {
      toggleDarkMode: function () {
        this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
        this.darkMode = !this.darkMode;
      }
    },
    computed: {
      switchLabel: function () {
        return this.darkMode ? 'light' : 'dark';
      }
    }
};
</script>