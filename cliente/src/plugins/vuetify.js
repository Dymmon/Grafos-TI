import Vue from "vue";
import Vuetify from "vuetify/lib";
import es from "vuetify/es5/locale/es";

Vue.use(Vuetify);

const vuetify = new Vuetify({
  lang: {
    locales: {
      es
    },
    current: "es",
  },
  icons: {
    iconFont: "mdi",
  },
  theme: {
    themes: {
      light: {
        primary: "#46c292",
      },
    },
  },
});

export default vuetify;