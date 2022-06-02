<template>
    <div class="d-flex justify-center align-center" id="div">
        <v-card class="d-flex flex-column justify-center align-center rounded-xl" width="500" height="600"  :elevation="10">
            <v-card-title class="mt-200px">Sign Up</v-card-title>

            <v-text-field label="Username" v-model="username"></v-text-field>
            <v-text-field type="email" label="Email" v-model="email"></v-text-field>
            <v-text-field type="password" label="Password" v-model="password"></v-text-field>
            <v-text-field type="password" label="Confirm Password" v-model="confirm_password"></v-text-field>
            <v-text-field label="Height" v-model="height"></v-text-field>
            <v-text-field label="Weight" v-model="weight"></v-text-field>
            <v-btn class="green" width="70" height="30" v-on:click="signup()">Signup</v-btn>

            
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