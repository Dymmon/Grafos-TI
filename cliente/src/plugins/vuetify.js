import Vue from "vue";
import Vuetify from "vuetify/lib";
import es from "vuetify/es5/locale/es";
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

const vuetify = new Vuetify({
  lang: {
    locales: { es },
    current: "es",
  },
  icons: {
    iconFont: "mdi",
  },
  theme: {
    themes: {
        light: {
          primary: colors.purple,
          secondary: colors.grey.darken1,
          accent: colors.shades.black,
          error: colors.red.accent3,
        },
        dark: {
          primary: colors.blue.lighten3,
        },
      },
  },
});

export default vuetify;
