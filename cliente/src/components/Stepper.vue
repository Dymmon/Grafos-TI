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
        >Centros de distribución</v-stepper-step
      >
      <v-divider></v-divider>
      <v-stepper-step step="3" :complete="pasoActual > 3"
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
          :onCancelar="onCancelar"
          :onSiguiente="
            () => {
              pasoActual = 2;
            }
          "
        ></input-archivo>
      </v-stepper-content>
      <v-stepper-content step="2">
        <centro-distribucion
          :onCancelar="onCancelar"
          :onActualizar="() => {}"
          :centros="centros"
          :puntos="puntos"
          :onDevolverse="
            () => {
              pasoActual = 1;
            }
          "
          :onSiguiente="
            () => {
              pasoActual = 3;
            }
          "
        ></centro-distribucion>
      </v-stepper-content>
      <v-stepper-content step="3">
        <punto-venta
          :onCancelar="onCancelar"
          :onGuardar="onGuardar"
          :onDevolverse="
            () => {
              pasoActual = 2;
            }
          "
        ></punto-venta>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>

<script>
import InputArchivo from "./InputArchivo";
import CentroDistribucion from "./CentroDistribucion";
import PuntoVenta from "./PuntoVenta";

export default {
  name: "Stepper",
  props: ["onFinalizar"],
  components: {
    InputArchivo,
    CentroDistribucion,
    PuntoVenta,
  },
  data() {
    return {
      pasoActual: 1,
      puntos: [],
      centros: [],
      camiones: [],
    };
  },
  watch: {
    pasoActual() {
      console.log("PASO ACTUAL: ", this.pasoActual);
    },
  },
  mounted() {
    this.pasoActual = 1;
  },
  methods: {
    onActualizar(puntos, centros) {
      this.puntos = puntos;
      this.centros = centros;
    },
    onActualizarSegundo(puntos, centros, camiones) {
      this.puntos = puntos;
      this.centros = centros;
      this.camiones = camiones;
    },
    onGuardar() {},
    onCancelar() {
      this.pasoActual = 1;
      this.puntos = [];
      this.centros = [];
    },
  },
  computed: {},
};
</script>
