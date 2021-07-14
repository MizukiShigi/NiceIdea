<template>
  <div>
    <Header />
    <v-container>
      <h2 class="mb-5">アイデア</h2>
      <p>{{ idea.content }}</p>
      <v-btn
        color="success"
        class="mr-2"
        :to="{ name: 'editer', params: { id: idea.id } }"
        >編集</v-btn
      >
      <v-btn color="error" @click="deleteIdeaData">削除</v-btn>
    </v-container>
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
// import { apiService } from "../common/api.service.js";

export default {
  name: "idea",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      idea: {},
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getIdeaData() {
      axios
        .get(`/api/ideas/${this.id}/`, {
          headers: { Authorization: "JWT " + localStorage.getItem("token") },
        })
        .then((response) => (this.idea = response.data))
        .then(() => this.setPageTitle(this.idea.company_name))
        .catch((error) => {
          console.log(error);
          this.$swal({
            type: "warning",
            title: "ログイン",
            text: "再ログインしてください",
            showConfirmButton: false,
            showCloseButton: false,
            timer: 1000,
          });
          this.$router.push("/login");
        });
    },
    deleteIdeaData() {
      axios
        .delete(`/api/ideas/${this.id}/`, {
          headers: { Authorization: "JWT " + localStorage.getItem("token") },
        })
        .then(() =>
          this.$router.push({
            name: "home",
          })
        )
        .catch((error) => {
          console.log(error);
          this.$swal({
            type: "warning",
            title: "ログイン",
            text: "再ログインしてください",
            showConfirmButton: false,
            showCloseButton: false,
            timer: 1000,
          });
          this.$router.push("/login");
        });
    },
  },
  created() {
    this.getIdeaData();
  },
};
</script>

<style>
</style>