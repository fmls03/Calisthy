<template>
    <v-app>
        <div class="d-flex flex-wrap justify-center">
            <v-card :elevation="6" class="d-flex flex-column justify-center align-center ma-8" height="300" width="350"
                @click="openUsersDialog()">
                <v-card-title>UTENTI</v-card-title>
            </v-card>

            <v-card :elevation="6" class="d-flex flex-column justify-center align-center ma-8" height="300" width="350"
                @click="openExercisesDialog()">
                <v-card-title>ESERCIZI</v-card-title>
            </v-card>
        </div>

        <v-dialog v-model="users_dialog" width="800">
            <v-card>
                <v-card-title>Utenti</v-card-title>
                <table>
                    <tr>
                        <th>
                            <h5 class="ml-2"></h5>
                        </th>
                        <th>
                            <h5 class="ml-3">Username</h5>
                        </th>
                        <th>
                            <h5 class="ml-5">Altezza(cm)</h5>
                        </th>
                        <th>
                            <h5 class="ml-4">Peso(Kg)</h5>
                        </th>
                        <th>
                            <h5 class="ml-4">Email</h5>
                        </th>
                    </tr>

                    <tr v-for="(u, index) in users" :key="index">
                        <th>
                            <h6 class="ml-2">-</h6>
                        </th>
                        <th>
                            <h5 class="ml-3">{{ u.username }}</h5>
                        </th>

                        <th>
                            <h6 class="ml-5">{{ u.height }}</h6>
                        </th>
                        <th>
                            <h6 class="ml-4">{{ u.weight }}</h6>
                        </th>
                        <th>
                            <h6 class="ml-4">{{ u.email }}</h6>
                        </th>
                        <th>
                            <v-btn @click="confirm_delete_dialog = true" class="ml-6 align-self-center" color="error"
                                x-small>Elimina</v-btn>
                        </th>

                        <v-dialog width="350" v-model="confirm_delete_dialog" persistent>
                            <v-card>
                                <v-card-title>Sei sicuro di eliminarlo?</v-card-title>
                                <v-card-actions>
                                    <v-btn class="mt-2 ml-1" small @click="deleteUser(u.id)" text color="error">Si</v-btn>
                                    <v-spacer></v-spacer>
                                    <v-btn small @click="confirm_delete_dialog = false" text color="error">no</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </tr>
                </table>
            </v-card>
        </v-dialog>



        <v-dialog v-model="exercises_dialog" width="800">
            <v-card>
                <v-card-title>Esercizi</v-card-title>
                <table>
                    <tr>
                        <th>
                            <h5 class="ml-2"></h5>
                        </th>
                        <th>
                            <h5 class="ml-3">Nome</h5>
                        </th>
                        <th>
                            <h5 class="ml-5">Path</h5>
                        </th>

                    </tr>

                    <tr v-for="(ex, index) in exercises" :key="index">
                        <th>
                            <h6 class="ml-2">-</h6>
                        </th>
                        <th>
                            <h5 class="ml-3">{{ ex.name }}</h5>
                        </th>
                        <th>
                            <h6 class="ml-5">{{ ex.path }}</h6>
                        </th>
                        <th>
                            <v-btn @click="openEditDialog(ex.id, ex.name, ex.path)" class="ml-6 align-self-center" color="primary" x-small>
                                Modifica</v-btn>
                        </th>
                        <th>
                            <v-btn  class="ml-3 align-self-center" color="error" x-small>
                                Elimina</v-btn>
                        </th>

                        <v-dialog v-model="edit_exercise_dialog" width="500" persistent>
                            <v-card>
                                <v-card-title>Modifica esercizio</v-card-title>

                                <v-text-field class="ml-6" label="name" v-model="name"></v-text-field>
                                <v-text-field class="ml-6" label="path" v-model="path"></v-text-field>
                                <v-card-actions>
                                    <v-btn v-if="name && path" @click="editExercise()" color="primary" text>Salva</v-btn>
                                    <v-btn v-else disabled color="primary" text>Salva</v-btn>
                                    <v-spacer></v-spacer>
                                    <v-btn color="error" @click="closeEditDialog()" text>Annulla</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </tr>
                </table>
            </v-card>
        </v-dialog>


    </v-app>
</template>


<script>
import axios from 'axios'

export default {
    data() {
        return {
            users_dialog: false,
            exercises_dialog: false,
            confirm_delete_dialog: false,
            edit_exercise_dialog: false,
            users: [],
            exercises: [],
            id: '',
            name: '',
            path: '',

        }
    },
    methods: {
        async getUsers() {
            let resp = await axios.get('admin/users')
            this.users = resp.data
        },
        async getExercises() {
            let resp = await axios.get('/admin/exercises')
            this.exercises = resp.data
        },

        openUsersDialog() {
            this.users_dialog = true
        },
        openExercisesDialog() {
            this.exercises_dialog = true
        },

        async deleteUser(userID) {
            await axios.delete(`admin/users/delete/${userID}`)
            this.getUsers()
            this.confirm_delete_dialog = false
        },

        async editExercise(){
            const paylaod = {
                id: this.id,
                name: this.name,
                path: this.path,
            }
            await axios.put(`admin/exercises/edit`, paylaod)
            this.getExercises()
            this.closeEditDialog()
        },

        openEditDialog(ExID, ExNAME, ExPATH){
            this.id = ExID,
            this.name = ExNAME,
            this.path = ExPATH,
            this.edit_exercise_dialog = true
        },

        closeEditDialog(){
            this.edit_exercise_dialog = false,
            this.name = ''
            this.path = ''
        }
    },
    mounted() {
        this.$vuetify.theme.dark = this.$session.get('theme');
        this.getUsers();
        this.getExercises()
    }
}
</script>

