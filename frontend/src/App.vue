<template>
<v-app>
  <NavBar></NavBar>
    <router-view/>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar.vue'


export default {
  name: 'App',
  components:{
    NavBar
  },
  data() {
    return{
    }
  }
};
</script>
