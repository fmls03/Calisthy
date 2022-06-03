<template>
    <div class="d-flex justify-center align-center" id="div">
        <v-card class="d-flex flex-column align-center rounded-xl" width="500" height="570" :elevation="10">
            <v-card-title >Sign Up</v-card-title>

        <v-form class="d-flex flex-column justify-center align-center ">
            <v-text-field class="small" label="Username" v-model="username"></v-text-field>
            <v-text-field type="email" label="Email" v-model="email"></v-text-field>
            <v-text-field type="password" label="Password" v-model="password"></v-text-field>
            <v-text-field type="password" label="Confirm Password" v-model="confirm_password"></v-text-field>
            <v-text-field type="number" label="Height" v-model="height"></v-text-field>
            <v-text-field type="number" label="Weight" v-model="weight"></v-text-field>
            <v-btn v-if="username && password && email && confirm_password && height && weight" class="green" width="70" height="30" v-on:click="signup()">Signup</v-btn>
            <v-btn v-else disabled class="green" width="70" height="30" v-on:click="signup()">Signup</v-btn>
            
            <p class="ma-5">If you already have an account click <router-link to="/login">here</router-link></p>

        </v-form>            
        </v-card>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    name: 'SignupPage',
    data() {
        return{
            username: '',
            email: '',
            password: '',
            confirm_password: '',
            height: '',
            weight: ''
        };
    },
    methods: {
        async signup(){
            const payload = {
                username: this.username,
                email: this.email,
                password: this.password,
                height: this.height,
                weight: this.weight 
            };
            await axios.post(`/api/signup`, payload)
            .then(response => {console.log(response)
            });
        
        }
    }
}
</script>


<style>
#div{
    height: '100%'
}
</style>