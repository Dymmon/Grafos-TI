<template>
  <div class="is-full-h" style="padding: 20px;">
    <v-card>
      <div
        class="container"
        style="height: calc(100vh - 120px); padding: 40px; overflow-y: scroll"
      >
        <p class="title text-center">Trabajo Integral: Hoja de rutas</p>
        <v-btn
          rounded
          color="primary"
          text
          outlined
          @click="modalStepper = true"
          >Ingresar información</v-btn
        >
        <div v-if="rutas != null">
          <p class="title text-center">Resultado</p>
          <div v-for="(camion, i) in rutas" :key="i">
            <p class="title-2">{{ camion.camion }}</p>
            <p
              class="subtitle-2 ml-3"
              v-for="(ruta, j) in camion.ruta"
              :key="j"
            >
              -
              {{
                camion.productos == 0
                  ? `El camión no necesitó salir.`
                  : `Se dirige a ${
                      ruta.esCentroDistribucion
                        ? `CD${ruta.id}(${ruta.coordenadas.x}, ${ruta.coordenadas.y}) y se abastece de ${camion.productos} productos.`
                        : `PV${ruta.id}(${ruta.coordenadas.x}, ${ruta.coordenadas.y}) y entrega ${ruta.productos} productos.`
                    }`
              }}
            </p>
          </div>
        </div>
        <div v-else>
        <p class="subtitle-2 text-center">No se ha cargado ningún archivo para calcular.</p>
        </div>
      </div>
      <v-btn
        absolute
        dark
        fab
        bottom
        right
        color="secondary"
        @click="modalIntegrantes = true"
      >
        <v-icon>mdi-account-circle-outline</v-icon>
      </v-btn>
    </v-card>

    <v-dialog v-model="modalIntegrantes">
      <v-card
        ><div class="container" style="height: 100%; padding: 40px;">
          <p class="title">Universidad Tecnológica Metropolitana</p>
          <p class="subtitle">INFB8061 - Grafos y Lenguajes Formales</p>

          <div style="display: flex; justify-content: space-between;">
            <persona
              v-for="integrante in integrantes"
              :key="integrante.nombre"
              :redes="integrante.redes"
              :nombre="integrante.nombre"
              :imagen="integrante.imagen"
            />
          </div></div
      ></v-card>
    </v-dialog>
    <v-dialog v-model="modalStepper">
      <stepper
        :onFinalizar="
          (data) => {
            guardar(data);
          }
        "
        :onCancelar="
          () => {
            modalStepper = false;
          }
        "
      ></stepper>
    </v-dialog>
  </div>
</template>

<script>
import Persona from "../components/Persona.vue";
import Stepper from "../components/Stepper.vue";
export default {
  components: {
    Persona,
    Stepper,
  },
  methods: {
    guardar(data) {
      this.rutas = data;
      this.modalStepper = false;
    },
  },
  data: () => ({
    modalIntegrantes: false,
    modalStepper: false,
    rutas: null,
    integrantes: [
      {
        nombre: "Javier Garrido",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80979585-88368600-8df5-11ea-8d6b-0a2541ba09bb.png",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/Scalim",
            icono: "github-circle",
            color: "#000",
          },
        ],
      },
      {
        nombre: "Mariam Maldonado",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80976941-114bbe00-8df2-11ea-9d68-6c42c6846944.jpeg",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/mariam6697",
            icono: "github-circle",
            color: "#000",
          },
          {
            nombre: "Twitter",
            url: "https://twitter.com/mariam_vmm",
            icono: "twitter",
            color: "#1da1f2",
          },
        ],
      },
      {
        nombre: "Carlos Montuyao",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80985782-ad2ef700-8dfd-11ea-93ab-23f6434a7422.png",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/Dymmon",
            icono: "github-circle",
            color: "#000",
          },
        ],
      },
      {
        nombre: "Jorge Verdugo",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80977076-3e986c00-8df2-11ea-80c9-d62518f47e34.jpeg",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/mapacheverdugo",
            icono: "github-circle",
            color: "#000",
          },
          {
            nombre: "Instagram",
            url: "http://instagram.com/mapacheverdugo",
            icono: "instagram",
            color: "#c13584",
          },
          {
            nombre: "Twitter",
            url: "https://twitter.com/mapacheverdugo",
            icono: "twitter",
            color: "#1da1f2",
          },
        ],
      },
      {
        nombre: "Javiera Vergara",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80976999-23c5f780-8df2-11ea-8343-061da9c2b69c.jpeg",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/PollitoMayo",
            icono: "github-circle",
            color: "#000",
          },
          {
            nombre: "Twitter",
            url: "https://twitter.com/pollitomayonesa",
            icono: "twitter",
            color: "#1da1f2",
          },
          {
            nombre: "DeviantArt",
            url: "https://www.deviantart.com/pollitomayo",
            icono: "deviantart",
            color: "#4dc47d",
          },
        ],
      },
    ],
  }),
};
</script>
