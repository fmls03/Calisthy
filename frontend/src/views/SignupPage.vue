<template>
    <div class="d-flex justify-center align-center" id="div">
        <v-card class="d-flex flex-column justify-center align-center" width="500" height="500" >
            <v-card-title class="mt-200px">Sign Up</v-card-title>

            <v-text-field label="Username" v-model="username"></v-text-field>
        </v-card>
    </div>
</template>


<script>
export default {
    name: 'SignupPage'
}
</script>


<style>
#div{
    height: '100%'
}
</style>