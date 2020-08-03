<template>
  <section class="fill-height">
    <v-stepper class="fill-height" alt-labels="true" style="padding: 10px 0 10px 0;" v-model="pasoActual">
      <v-stepper-header>
        <v-stepper-step step="1" :complete="pasoActual > 1">Archivo</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step step="2" :complete="pasoActual > 2">Centros de distribución</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step step="3" :complete="pasoActual > 3">Puntos de venta</v-stepper-step>
      </v-stepper-header>
      <v-stepper-items>
        <v-stepper-content step="1">
          <input-archivo></input-archivo>
        </v-stepper-content>
        <v-stepper-content step="2">
          
        </v-stepper-content>
        <v-stepper-content step="3">
          
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </section>
</template>

<script>
import InputArchivo from "./InputArchivo";

export default {
  name: "Stepper",
  props: [
    "onFinalizar"
  ],
  components: {
      InputArchivo
  },
  data() {
    return {
      pasoActual: 0
    };
  },
  watch: {
      pasoActual(){
          console.log("PASO ACTUAL: ", this.pasoActual);
      }
  },
  mounted() {},
  computed: {
  }
};
</script>