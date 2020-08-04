<template>
  <v-stepper
    class="fill-height"
    :alt-labels="true"
    style="padding: 0px 0 20px 0;"
    v-model="pasoActual"
  >
    <v-stepper-header>
      <v-stepper-step step="1" :complete="pasoActual > 1"
        >Archivo</v-stepper-step
      >
      <v-divider></v-divider>
      <v-stepper-step step="2" :complete="pasoActual > 2"
        >Puntos de venta</v-stepper-step
      >
    </v-stepper-header>
    <v-stepper-items>
      <v-stepper-content step="1">
        <input-archivo
          :onActualizar="
            (puntos, centros) => {
              onActualizar(puntos, centros);
            }
          "
          :onCancelar="cancelar"
          :onSiguiente="
            () => {
              pasoActual = 2;
            }
          "
        ></input-archivo>
      </v-stepper-content>
      <v-stepper-content step="2">
        <punto-venta
        :puntos="puntos"
          :onCancelar="cancelar"
          :onGuardar="(puntos)=>{onGuardar(puntos)}"
          :onDevolverse="
            () => {
              pasoActual = 1;
            }
          "
        ></punto-venta>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>

<script>
import InputArchivo from "./InputArchivo";
import PuntoVenta from "./PuntoVenta";
import axios from "axios";

export default {
  name: "Stepper",
  props: ["onFinalizar", "onCancelar"],
  components: {
    InputArchivo,
    PuntoVenta,
  },
  data() {
    return {
      pasoActual: 1,
      puntos: [],
      centros: []
    };
  },
  mounted() {
    this.pasoActual = 1;
    this.puntos = [];
    this.centros = [];
  },
  methods: {
    onActualizar(puntos, centros) {
      this.puntos = puntos;
      this.centros = centros;
    },
    onGuardar(puntos) {
      this.puntos = puntos;
      axios.post(`${this.$apiUrl}/rutas`, {centrosDistribucion: this.centros, puntosVenta: this.puntos})
      .then(r => {
        this.onFinalizar(r.data.rutas);
      })
      .catch(e => {
        console.log(e);
      })
    },
    cancelar() {
      this.pasoActual = 1;
      this.puntos = [];
      this.centros = [];
      this.onCancelar();
    },
  },
  computed: {},
};
</script>
