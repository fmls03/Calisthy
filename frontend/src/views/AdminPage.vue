<template>
    <v-app >    
        <div class="d-flex flex-wrap">
            <v-card :elevation="4" class="ma-8" height="300" width="250" @click="getUsers()">
                <v-card-title>Users</v-card-title>
            </v-card>

            <v-dialog v-model="usersDialog" max-width="800" max-height="800">
                <v-card>
                    <v-card-title>miao</v-card-title>
                </v-card>
            </v-dialog>

            <v-card class="ma-8"  height="300" width="250">
                <v-card-title>Exercises</v-card-title>
            </v-card>

            
        </div>
    </v-app>
    
</template>


<script>
import axios from 'axios'

export default {
    data: {
        exercisesDialog: false,
        usersDialog: false,
        users: [],
        exercises: []
    },
    methods: {
        async getUsers(){
            resp = await axios.get('admin/users')
            this.users = resp.data
            this.usersDialog = true
        },
        async getExercises() {
            let resp = await axios.get('admin/exercises')
            this.exercises = resp.data
        },

        openUsersDialog(){
            this.usersDialog = true
            this.getUsers()
        }
    },
    mounted() {
        this.$vuetify.theme.dark = this.$session.get('theme');
    }
}
</script>