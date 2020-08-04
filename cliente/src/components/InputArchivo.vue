<template>
  <v-container>
    <h3 class="headline mb-8">Ingresar archivo</h3>
    <v-spacer></v-spacer>
    <v-file-input
      v-model="archivo"
      color="deep-purple accent-4"
      placeholder="Seleccionar archivo"
      prepend-icon="mdi-paperclip"
      outlined
      show-size
      accept=".txt"
    >
    </v-file-input>
    <v-divider class="pb-8"></v-divider>
    <v-row align="center" justify="space-between">
      <v-btn color="primary" depressed rounded @click="onCancelar"
        >Cancelar</v-btn
      >
      <v-btn color="primary" depressed rounded @click="continuar"
        >Siguiente</v-btn
      >
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "input-archivo",
  props: ["onSiguiente", "onCancelar", "onActualizar"],
  data() {
    return {
      archivo: null,
    };
  },
  watch: {},
  methods: {
    continuar() {
      let formData = new FormData();
      formData.append("archivo", this.archivo);
      axios
        .post(`${this.$apiUrl}/resumen`, formData)
        .then((r) => {
          console.log("DATA: ", r.data);
          this.onActualizar(r.data.puntosVenta, r.data.centrosDistribucion);
          this.onSiguiente();
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
