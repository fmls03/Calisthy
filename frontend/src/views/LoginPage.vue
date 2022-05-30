<template>
    <div class="d-flex align-center justify-center" id="div">
        <v-card class="d-flex flex-column justify-center align-center rounded-xl" width="400" height="300" :elevation="10">
            <v-card-title>
                Login
            </v-card-title>
            <v-card-text >
                <v-form class="d-flex align-center flex-column mx-auto" >
                    <v-text-field label="username" v-model="username"></v-text-field>
                    <v-text-field type="password" label="password" v-model="password"></v-text-field>
                    <v-btn class="green" width="70" height="30" v-on:click="sendData()">Login</v-btn>
                </v-form>
                </v-card-text>
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
            password: ''
        };
    },
    methods: {
        async sendData(){
                const payload = {
                    username: this.username,
                    password: this.password
                };
            await axios.post(`/api/login`, payload)
            .then(response => {console.log(response);
            });
        }
    }

}


</script>

<style>
#div{
    height: 100%;
}
</style>



