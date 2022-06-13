<template>
    <v-app>
        <v-dialog class="d-flex" v-model="dialog" max-width="800" max-height="800" @input="get_plan_exercise(plan.id)">
            <template class="d-flex" v-slot:activator="{ on, attrs }">
                <h1 class="mt-10 ml-4">Le tue schede</h1>
                <div class="d-flex flex-wrap" >   
                    <v-card v-for="(plan, index) in plans" :key="index" min-width="230" max-width="250" min-height="300" class="ml-4 mt-8" @click="get_plan_exercise(plan.id)">
                        <v-card-title method="">{{ plan.title }}</v-card-title>
                    </v-card>
                </div>
            </template>
            <v-card>
                <div v-for="(ex, index) in exercises" :key="index">
                    <v-card-title>
                        {{ex.exercise}}
                    </v-card-title>

                    <h4 class="font-weight-light">{{ex.exercise}}</h4>
                    
                </div>

                <v-card-actions>
                    <v-spacer></v-spacer>
                        <v-btn @click="dialog=false" text error>
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
            items: [1,2,3,4,5],
            plans: [],
            exercises: []
        }
    },
    methods: {
        async get_training_plans(){
            const payload = {
                username: this.$session.get('username')
            };

            let resp = await axios.post(`/user/home`, payload);

            console.log(resp);
            this.plans = resp.data;
            console.log(this.plans);
        },

        async get_plan_exercise(planID){
            this.dialog = true
            let planid = planID
            console.log(planid)
            const payload = {
                plan_id: planid
            }
            let resp = await axios.post(`/user/home/exercises`, payload);
            this.exercises = resp.data;
            console.log(resp.data.id)
            console.log(this.exercises)
        },

    },

    mounted() {
        this.$vuetify.theme.dark = this.$session.get('theme');
        this.get_training_plans()
    }
}
</script>
