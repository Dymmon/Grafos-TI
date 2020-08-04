<template>
  <div class="fill-height d-flex align-center justify-center">
    <v-col align="center" justify="space-around" class="fill-height">
      <v-row>
        <v-col cols="6"><h3>Número de camiones</h3></v-col>
        <v-col cols="2">
          <v-btn rounded class="ma-0 pa-0" @click="cantidad = cantidad - 1"
            >-</v-btn
          >
        </v-col>
        <v-col cols="2">
          <v-text-field outlined v-model="cantidad"></v-text-field>
        </v-col>
        <v-col cols="2">
          <v-btn rounded class="ma-0 pa-0" @click="cantidad = cantidad + 1"
            >+</v-btn
          >
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <div>
        <div v-for="(centro, i) in centros" :key="i">
        <v-row>
          <v-col cols="3"><h3>CD{{centro.id}}</h3></v-col>
          <v-col cols="4">
            <v-select :items="camiones" item-text="nombre" dense outlined></v-select>
          </v-col>
        </v-row>
        </div>
      </div>
      <v-divider></v-divider>
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
  props: ["onSiguiente", "onDevolverse", "centros", "puntos"],
  data() {
    return {
      cantidad: this.centros.length,
      camiones: [],
      seleccionCamiones: []
    };
  },
  watch: {
    centros() {
      this.cantidad = this.centros.length;
    },
    cantidad(){
        let auxiliar = [];
        for (let index = 1; index <= this.cantidad; index++) {
            let dato = {
                nombre: "Camión " + index
            };
            auxiliar.push(dato);
        }
        this.camiones = auxiliar;
        console.log("CAMIONES: ", this.camiones);
    }
  },
  methods: {
    devolverse() {
      this.onDevolverse();
    },
    continuar() {
      this.onSiguiente();
    },
  },
};
</script>
