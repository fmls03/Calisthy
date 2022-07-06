<template>
    <v-card>
        <v-card-title>Aggiungi esercizio</v-card-title>
        <v-text-field class="ml-6" label="name" v-model="name"></v-text-field>
        <v-text-field class="ml-6" label="path" v-model="path"></v-text-field>
        <v-card-actions>
            <v-btn v-if="name && path" color="primary" text @click="save_new_exercise()">Salva</v-btn>
            <v-btn v-else disabled color="primary" text>Salva</v-btn>
            <v-spacer></v-spacer>
            <v-btn @click="send_close_dialog()" color="error" text>Annulla</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import axios from 'axios'

export default{
    props: ['add_exercise_dialog'],
    data(){
        return{
            close_dialog: this.add_exercise_dialog,
            name: '',
            path: '',

        }
    },
    methods: {
        send_close_dialog(){
            this.close_dialog = false
            this.$emit('close', this.close_dialog)
        },
        async save_new_exercise(){
            const payload = {
                name: this.name,
                path: this.path,
            }
            let resp = await axios.post('admin/add/exercise', payload)
            if (resp.data === 'Exercise added'){
                this.send_close_dialog()
            }
        }
    }
}
</script>