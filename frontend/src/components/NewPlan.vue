<template>
    <v-card class="d-flex flex-column">
        <v-card-title>
            Crea nuova scheda
        </v-card-title>
            <v-text-field class="ml-5" label="Nome della scheda" v-model="plan_name"></v-text-field>
            <table class="ml-5 mb-5">
                <tr>
                    <th>N</th>
                    <th>Esercizio</th>
                    <th>Reps</th>
                    <th>Sets</th>
                    <th>Rest</th>
                </tr>
                <tr v-for="(ex, index) in exercises" :key="index">
                    <th class="font-weight-light" >{{index + 1}}</th>
                    <th class="font-weight-light">{{ex.exercise}}</th>
                    <th class="font-weight-light">{{ex.reps}}</th>
                    <th class="font-weight-light">{{ex.sets}}</th>
                    <th class="font-weight-light"   >{{ex.rest}}s</th>
                </tr>
            </table>

            <div class="d-flex flex-row">
                <v-select label="Esercizio" :items="list_exercises" item-text="name" v-model="exercise"  outlined></v-select>
                <v-text-field type="number" label="reps" v-model="reps"></v-text-field>
                <v-text-field type="number" label="sets" v-model="sets"></v-text-field>
                <v-text-field type="number" label="rest" v-model="rest"></v-text-field>
            </div>            
            <h4 class="align-self-center mb-3  red--text" color="brown">{{error}}</h4>
            <v-btn class="align-self-center" @click="add_new_exercise()" color="primary" width="200">Aggiungi esercizio</v-btn>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="send_new_plan" text color="primary">Salva</v-btn>
            <v-btn @click="send_close" text color="error">Annulla</v-btn>
        </v-card-actions>
        
    </v-card>
</template>

<script>
import axios from 'axios'

export default{
    props: ['create_dialog'],
    data(){
        return{
            close_dialog: this.create_dialog,
            list_exercises: [],
            plan_name: '',
            exercise: '',
            reps: '',
            sets: '',
            rest: '',
            exercises:[],
            error: ''
        }
    },
    methods: {
        send_close(){
            
            this.close_dialog = false
            this.$emit('close', this.close_dialog)
            location.reload()
        },

        add_new_exercise(){
            if (this.exercise != "" && this.reps != "" && this.sets != "" && this.rest != "" ){ 
                this.error = ''
                this.exercises.push({
                    exercise: this.exercise,
                    reps: this.reps,
                    sets: this.sets,
                    rest: this.rest,
                });
                console.log(this.exercises)
            }
            else{
                this.error = '* Compila tutti i campi *'
            }
        },

        async get_exercises_list(){
            let resp = await axios.get('exercises/list')
            this.list_exercises = resp.data
            console.log(this.list_exercises.name)
        },

        async send_new_plan(){
            if (this.plan_name === ''){
                this.error = '* Devi inserire il nome della scheda *'
            }
            else if (!this.exercises.lenght){
                this.error = '* Devi inserire almeno un esercizio *'
            }
            else{
                this.error = ''
                const payload = {
                    plan_name: this.plan_name,
                    exercises: this.exercises,
                    creator: this.$session.get('username')
                }
                console.log(payload.exercises)
                let resp = await axios.post('user/new_plan', payload)
                console.log(resp)

                this.send_close()
            }
            }

        
    },
    mounted() {
        this.get_exercises_list()
    }
}
</script>

<style>
.v-text-field{
    margin-right: 22px;
}

.v-select{
    margin-left: 22px !important;
    margin-right: 22px !important;
}


th {
  text-align: left;
}

</style>