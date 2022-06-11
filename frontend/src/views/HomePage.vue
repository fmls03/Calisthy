<template>
    <v-app>
        <v-dialog class="d-flex" v-model="dialog" max-width="800" max-height="800">
            <template class="d-flex" v-slot:activator="{ on, attrs }">
                <h1 class="mt-10 ml-4">Le tue schede</h1>
                <div class="d-flex flex-wrap" >   
                    <v-card v-for="(plan, index) in plans" :key="index" min-width="230" max-width="250" min-height="300" class="ml-4 mt-8" @click="dialog=true">
                        <v-card-title>{{ plan.title }}</v-card-title>
                    </v-card>
                </div>
            </template>
            <v-card>
                <v-card-title>
                    
                </v-card-title>


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
            plans: []
        }
    },
    methods: {
        async send_session_data(){
            const payload = {
                username: this.$session.get('username')
            };

            let resp = await axios.post(`/user/home`, payload);

            console.log(resp);
            this.plans = resp.data;
            console.log(this.plans);
        }

    },

    mounted() {
        this.$vuetify.theme.dark = this.$session.get('theme');
        this.send_session_data()
    }
}
</script>
