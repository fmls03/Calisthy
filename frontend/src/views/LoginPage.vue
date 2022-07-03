<template>
    <div class="d-flex align-center flex-column justify-center" id="div">
        <v-alert :value="alert" dense text type="error" transition="scroll-y-transition" elevation="8" >{{msg}}</v-alert>
        <v-card class="d-flex flex-column justify-center align-center rounded-xl" width="400" height="320" elevation="10">
            <v-card-title class="mt-5">
                Login
            </v-card-title>
                <v-form class="d-flex align-center flex-column mx-auto" >
                    <v-text-field label="Username" v-model="username"></v-text-field>
                    <v-text-field type="password" label="Password" v-model="password" @click:append="show = !show" :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'" :type="show ? 'text' : 'password'"    ></v-text-field>
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
            msg: '',
            alert: false,
            show: false,
            error: 'error'
        };
    },
    methods: {
        async sendData(){
            this.alert = false;
            const payload = {
                username: this.username,
                password: this.password
            };
            let resp = await axios.post(`/api/login`, payload)
        
            if (resp.data === 'wrong password' || resp.data === 'wrong username'){
                this.alert = true;
                this.msg = resp.data;
            }
            else{
                                
                this.$session.set('username', resp.data.username)
                this.$session.set('email', resp.data.email)
                this.$session.set('theme', resp.data.theme)
                this.$session.set('height', resp.data.height)
                this.$session.set('weight', resp.data.weight)
                
                this.$vuetify.theme.dark = this.$session.get('theme');
                if (this.$session.get('username') === 'admin'){
                    window.location.replace('/admin');

                }
                else{
                    window.location.replace('/home');
                }
            }
        
        },
       
    }   

}


</script>

<style>
#div{
    height: 100%;
}

.v-text-field{
    width: 250px !important;
}
</style>



