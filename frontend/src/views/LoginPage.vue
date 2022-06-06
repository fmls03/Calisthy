<template>
    <div class="d-flex align-center justify-center" id="div">
        <v-card class="d-flex flex-column justify-center align-center rounded-xl" width="400" height="32
        0" :elevation="10">
            <v-card-title class="mt-5">
                Login
            </v-card-title>
                <v-form class="d-flex align-center flex-column mx-auto" >
                    <v-text-field label="Username" v-model="username"></v-text-field>
                    <v-text-field type="password" label="Password" v-model="password"></v-text-field>
                    <v-btn v-if="username && password" small class="green" width="70" height="30" v-on:click="sendData()">Login</v-btn>
                    <v-btn v-else disabled class="green" small width="70" height="30" v-on:click="sendData()">Login</v-btn>
                    <p class="ma-5">If you're not already registered click <router-link to="/signup">here</router-link></p>

                </v-form>
        </v-card>

    </div>

</template>

<script>
import axios from 'axios'

export default {
    name : 'LoginPage',
    data() {
        return {
            username: '',
            password: '',
        };
    },
    methods: {
        async sendData(){
            const payload = {
                username: this.username,
                password: this.password
            };
            let logged = await axios.post(`/api/login`, payload)
            
            console.log(logged.data)
            if (logged.data === 'user logged'){
                window.location.replace('/home');
            }
            else if (logged.data === 'wrong username'){
                window.location.replace('/signup');
            };
        }
    }

}


</script>

<style>
#div{
    height: 100%;
}
</style>



