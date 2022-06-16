<template>
    <v-card class="d-flex flex-column">
        <v-card-title>
            Crea nuova scheda
        </v-card-title>
            <p>
                <v-text-field label="Nome della scheda" v-model="plan_name"></v-text-field>
            </p>
            <div>
                <v-select label="Exercise" :items="list_exercises" item-text="name" v-mode="exercise_name" outlined></v-select>
                <v-input type="number" label="reps" v-model="exercise.reps"></v-input>
            </div>
            <p>{{exercise.name}}</p>
            <p>{{exercise.reps}}</p>
            <v-btn>Aggiungi esercizio</v-btn>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="send_close" text color="error">close</v-btn>
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
            new_plan: [
                {
                    exercise: 'miao',
                    reps: 'bau',
                    sets: 'ciao',
                    rest: 'oajd',
            }],
        }
    },
    methods: {
        send_close(){
            this.close_dialog = false
            this.$emit('close', this.close_dialog)
        },
        async get_exercises_list(){
            let resp = await axios.get('exercises/list')
            this.list_exercises = resp.data
            console.log(this.list_exercises.name)
        },

        
    },
    mounted() {
        this.get_exercises_list()
    }
}
</script>
