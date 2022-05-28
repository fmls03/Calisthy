<template>
    <div class="d-flex align-center justify-center" id="div">
        <v-card class="d-flex flex-column justify-center align-center" width="400" height="300">
            <v-card-title>
                Login
            </v-card-title>
            <v-card-text>
                <v-form>
                    <v-text-field label="username"></v-text-field>
                    <v-text-field type="password" label="password"></v-text-field>
                </v-form>
                <v-btn width="80">Login</v-btn>
            </v-card-text>
        </v-card>

    </div>

</template>

<style>
#div{
    height: 100%;
}
</style>