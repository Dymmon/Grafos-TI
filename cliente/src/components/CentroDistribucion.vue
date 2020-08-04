<template>
  <div class="fill-height d-flex align-center justify-center">
  <v-col align="center" justify="space-around" class="fill-height">
    <h3>Ingresar archivo</h3>
    <v-file-input
      v-model="files"
      color="deep-purple accent-4"
      placeholder="Seleccionar archivo"
      prepend-icon="mdi-paperclip"
      outlined
      :show-size="1000"
    >
    </v-file-input>
    <v-row align="center" justify="space-between">
    <v-btn outlined rounded @click="devolverse">Atrás</v-btn>
    <v-btn outlined rounded @click="continuar">Siguiente</v-btn>
    </v-row>
  </v-col>
  </div>
</template>

<script>
export default {
  name: "input-archivo",
  props: ["onSiguiente", "onDevolverse"],
  data() {
    return {
      files: null,
    };
  },
  methods: {
      devolverse(){
          this.onDevolverse();
      },
      continuar(){
          this.onSiguiente();
      }
  }
};
</script>
