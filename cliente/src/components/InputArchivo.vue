<template>
  <div class="fill-height d-flex align-center justify-space-between">
    <v-col align="center">
      <h3>Ingresar archivo</h3>
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
      <v-row align="center" justify="space-between">
        <v-btn outlined rounded @click="onCancelar">Cancelar</v-btn>
        <v-btn outlined rounded @click="continuar" :disabled="deshabilitado">Siguiente</v-btn>
      </v-row>
    </v-col>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "input-archivo",
  props: ["onSiguiente", "onCancelar", "onActualizar"],
  data() {
    return {
      archivo: null,
      deshabilitado: true,
    };
  },
  watch: {
    archivo(){
      if(this.archivo){
        this.deshabilitado = false;
      }
    },
  },
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
