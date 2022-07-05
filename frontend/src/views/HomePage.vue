<template>
    <v-app>
        <div class="d-flex flex-row align-center justify-space-between">
            <h1 class="mt-10 ml-4">Le tue schede</h1>
            <v-btn width="200" class="mt-10" color="primary" text v-on:click="create_new_plan()"> Crea nuova scheda
            </v-btn>
            <v-dialog max-width="1000px" v-model="create_dialog" persistent>
                <NewPlan :exercises="exercises" :create_dialog="create_dialog" @close="close_create_dialog"></NewPlan>
            </v-dialog>
        </div>

        <div class="d-flex flex-wrap">
            <v-card v-for="(plan, index) in plans" :key="index" min-width="230" max-width="250" min-height="300" :elevation="4"
                class="ml-4 mt-8" @click="get_plan_exercise(plan.id), get_Title_Plan(plan.title)">
                <v-card-title>{{ plan.title }}</v-card-title>
                <h5 class="ml-4 font-weight-light"> {{plan.description }} </h5>
            </v-card>
        </div>
        <v-dialog class="d-flex" v-model="plan_dialog" max-width="800" max-height="800" 
            @input="get_plan_exercise(plan.id)">

            <v-card>
                <v-card-title>{{ planTitle }}</v-card-title>
                
                <table>
                    <tr>
                        <th><h5 class="font-weight-light ml-6">N.</h5></th>
                        <th><h5 class="font-weight-light ml-2">Exercise</h5></th>
                        <th><h5 class="font-weight-light ml-4">Reps</h5></th>
                        <th><h5 class="font-weight-light ml-2">Sets</h5></th>
                        <th><h5 class="font-weight-light ml-2">Rest (s)</h5></th>
                    </tr>
                    <tr v-for="(ex, index) in exercises" :key="index" >
                        <th><h4 class="font-weight-bold ml-6">{{ index + 1 }})</h4></th>
                        <th><h4 class="font-weight-bold ml-2"> {{ ex.exercise }}</h4></th>
                        <th><h5 class="font-weight-light ml-4">{{ ex.reps }}</h5></th>
                        <th><h5 class="font-weight-light ml-2">{{ ex.sets }}</h5></th>
                        <th><h5 class="font-weight-light ml-2">{{ ex.rest }}s</h5></th>
                        <v-btn class="mr-3" color="primary" text x-small v-on:click="watch_video(ex.exercise)">Guarda
                        esecuzione</v-btn>

                    </tr>
                </table>
                <v-card-actions>
                    <v-btn class="mt-2 ml-1" small @click="delete_dialog = true" color="error">Elimina</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn small @click="plan_dialog = false" text color="error">close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-dialog width="560" height="315" v-model="video_dialog" persistent>
            <iframe width="560" height="315" :src="video.path" title="YouTube video player" frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen></iframe>
            <v-btn v-on:click="close_video_dialog()" color="error">close</v-btn>
        </v-dialog>

        <v-dialog width="350" v-model="delete_dialog" persistent>
            <v-card>
                <v-card-title>Sei sicuro di eliminarlo?</v-card-title>
                <v-card-actions>
                    <v-btn class="mt-2 ml-1" small @click="delete_plan" text color="error">Si</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn small @click="delete_dialog = false" text color="error">no</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <v-snackbar v-model="snackbar">
            {{alert}}
        </v-snackbar>
    </v-app>
</template>

<script>
import axios from 'axios'
import NewPlan from '../components/NewPlan.vue'
import $ from 'jquery'

export default {
    name: 'HomePage',
    components: {
        NewPlan,
    },
    data() {
        return {
            plan_dialog: false,
            video_dialog: false,
            create_dialog: false,
            delete_dialog: false,
            items: [1, 2, 3, 4, 5],
            plans: [],
            plan_id: '',
            exercises: [],
            planTitle: '',
            video: [],
            alert: '',
            snackbar: false
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
            this.plan_dialog = true
            this.plan_id = planID
            const payload = {
                plan_id: this.plan_id
            }
            let resp = await axios.post(`/user/home/exercises`, payload);
            this.exercises = resp.data;
        },

        async watch_video(ExName) {
            this.video_dialog = true
            let exName = ExName
            const payload = {
                exercise_name: exName
            }
            console.log(payload.exercise_name)
            let resp = await axios.post('/exercise/video', payload)
            this.video = resp.data
        },

        close_create_dialog(close_dialog){
            console.log(close_dialog)
            this.create_dialog = close_dialog
        },

        close_video_dialog() {
            this.video_dialog = false
            var video = $("iframe").attr("src");
            $("iframe").attr("src","");
            $("iframe").attr("src",video);
        },

        async create_new_plan() {
            this.create_dialog = true
        },

        async delete_plan(){
            const payload = {
                plan_id: this.plan_id
            }
            let resp = await axios.post('user/delete/plan', payload)
            console.log(resp)
            this.delete_dialog = false,
            this.plan_dialog = false,
            this.alert = resp.data,
            this.snackbar = true,
            setTimeout(this.snackbar = false, 5000)
            this.get_training_plans()
        }

        

    },

    mounted() {
        this.$vuetify.theme.dark = this.$session.get('theme');
        this.get_training_plans()
    }
}
</script>

<style>
#watch-video-col{
    
}
#mr{
    margin-right: 50vw;
}
</style>