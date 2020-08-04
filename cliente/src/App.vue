<template>
<v-app>
  <div
    style="
    height: 100%;"
  >
    <div style="padding: 30px; width: calc(100% - 50px); float: right">
      <div style="display: flex; justify-content: space-between;">
      <div class="text-center">
        <v-btn
        rounded
        flat
        outlined
        color="primary"
          >Autómata 2</v-btn
        >
      </div>
        <a href="https://github.com/Dymmon/Grafos-TI">
        <v-btn icon color="primary">
        <v-icon>github-circle</v-icon>
        </v-btn>
        </a>
      </div>

      <div class="d-flex" style="width: 100%;">
        <div
          class="card"
          style="width: 100%; height: calc(100vh - 80px - 45px); border-radius: 10px;"
        >
          <router-view />
        </div>
      </div>
    </div>
  </div>
</v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    // HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
