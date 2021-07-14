import Vue from "vue";
import VueRouter from "vue-router";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Home from "../views/Home.vue";
import Idea from "../views/Idea.vue"; // 追加
import IdeaEditer from '../views/IdeaEditer.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/login",
    name: "login",
    component: Login
  },
  {
    path: "/register",
    name: "register",
    component: Register
  },
  {
    path: "/idea/:id", // 追加
    name: "idea",
    component: Idea,
    props: true
  },
  {
    path: "/editer", // 追加
    name: "editer",
    component: IdeaEditer,
    props: true
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;