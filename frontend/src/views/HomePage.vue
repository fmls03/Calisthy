<template>
    <v-app>
        <h1 class="mt-10 ml-4">Le tue schede</h1>
        <div class="d-flex flex-row">
            <v-card width="250" height="300" class="ml-4 mt-8">
                <v-card-title>
                    miao
                </v-card-title>
            </v-card>
            <v-card width="250" height="300" class="ml-4 mt-8">
                <v-card-title>
                    miao
                </v-card-title>
            </v-card>
        </div>
    </v-app>
</template>

<script>
export default {
    name: 'HomePage',
    data () {
        return{
            
        }
    },
    mounted() {
        this.$vuetify.theme.dark = this.$session.get('theme');
    }
}

</script>