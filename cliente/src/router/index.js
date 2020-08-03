import Vue from "vue";
import VueRouter from "vue-router";
import Principal from "../views/Principal.vue";

Vue.use(VueRouter);

const routes = [{
    path: "/",
    name: "inicio",
    component: Principal
}];

const router = new VueRouter({
    mode: "history",
    base: process.env.VUE_APP_BASE_URL,
    routes
});

export default router;