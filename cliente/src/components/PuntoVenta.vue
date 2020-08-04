<template>
  <v-container>
    <div class="mx-6">
      <h3 class="headline mb-8 text-center">Puntos de Venta</h3>
      <v-row v-for="(punto, i) in puntos" :key="i">
        <v-col cols="3" class="ma-0 pa-0"
          ><h3 class="title-2">PV{{ punto.id }}</h3></v-col
        >
        <v-col cols="6" class="ma-0 pa-0"
          ><h3 class="subtitle-1">Cantidad de productos a entregar</h3></v-col
        >
        <v-col cols="3" class="ma-0 pa-0">
          <v-text-field outlined dense v-model="cantidades[i]"></v-text-field>
        </v-col>
      </v-row>
      <v-row align="center" justify="space-between">
        <v-btn outlined rounded @click="devolverse">Atrás</v-btn>
        <v-btn outlined rounded @click="guardar" :disabled="deshabilitado"
          >Guardar</v-btn
        >
      </v-row>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "input-archivo",
  props: ["onGuardar", "onDevolverse", "puntos"],
  data() {
    return {
      cantidades: [],
      deshabilitado: true,
    };
  },
  watch: {
    cantidades() {
      if (this.cantidades.length == this.puntos.length) {
        this.deshabilitado = false;
      }
    },
  },
  methods: {
    guardar() {
      var nuevo = this.puntos;
      for (let index = 0; index < nuevo.length; index++) {
        nuevo[index].productos = parseInt(this.cantidades[index]);
      }
      this.onGuardar(nuevo);
    },
    devolverse() {
      this.onDevolverse();
    },
  },
};
</script>
