<template>
    <v-app>
        <div class="d-flex flex-row align-center justify-space-between">
            <h1 class="mt-10 ml-4">Le tue schede</h1>
            <v-btn width="200" class="mt-10" color="primary" text > Crea nuova scheda</v-btn>
        </div>
        <v-dialog class="d-flex" v-model="dialog" max-width="800" max-height="800" @input="get_plan_exercise(plan.id)">
            <template class="d-flex" v-slot:activator="{ on, attrs }">


                <div class="d-flex flex-wrap">
                    <v-card v-for="(plan, index) in plans" :key="index" min-width="230" max-width="250" min-height="300"
                        class="ml-4 mt-8" @click="get_plan_exercise(plan.id), get_Title_Plan(plan.title)">
                        <v-card-title>{{ plan.title }}</v-card-title>
                    </v-card>
                </div>
            </template>
            <v-card>
                <v-card-title>{{ planTitle }}</v-card-title>

                <div v-for="(ex, index) in exercises" :key="index" class="d-flex flex-row">
                    <h4 class="font-weight-bold ml-6">{{index + 1}}) {{ ex.exercise }}</h4>
                    <h5 class="font-weight-light ml-6">{{ ex.reps }} x {{ ex.sets }} || {{ ex.rest }}s</h5>
                    <v-spacer></v-spacer>
                    <v-btn class="mr-3" color="primary" text x-small v-on:click="watch_video(ex.exercise)">Guarda esecuzione</v-btn>

                </div>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn small @click="dialog = false" text color="error">
                        close
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-app>
</template>

<script>
import axios from 'axios'

export default {
    name: 'HomePage',
    data() {
        return {
            dialog: false,
            items: [1, 2, 3, 4, 5],
            plans: [],
            exercises: [],
            planTitle: ''
        }
    },
    methods: {
        async get_training_plans() {
            const payload = {
                username: this.$session.get('username')
            };

            let resp = await axios.post(`/user/home`, payload);
            this.plans = resp.data;
        },

        get_Title_Plan(planTITLE) {
            this.planTitle = planTITLE;
        },

        async get_plan_exercise(planID) {
            this.dialog = true
            let planid = planID
            const payload = {
                plan_id: planid
            }
            let resp = await axios.post(`/user/home/exercises`, payload);
            this.exercises = resp.data;
        },

        async watch_video(ExName){
            let exName = ExName
            const payload = {
                exercise_name: exName
            }
            console.log(payload.exercise_name)
            let resp = await axios.post('/exercise/video', payload)
            console.log(resp.data)
            window.location.replace('http://localhost:5000/exercise/video')
        }

    },

    mounted() {
        this.$vuetify.theme.dark = this.$session.get('theme');
        this.get_training_plans()
    }
}
</script>
