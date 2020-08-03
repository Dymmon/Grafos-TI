import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import es from 'vuetify/es5/locale/es';

Vue.use(Vuetify);

export default new Vuetify({
    lang: {
        locales: {es},
        current: 'es',
    },
    icons: {
        iconFont: 'mdi',
    },
    theme: {
        themes: {
            light: {
                primary: '#46c292',
                secondary: '#eddf8c',
                accent: '#82BC00',
                error: '#b71c1c',
              },
        },
    },
});
