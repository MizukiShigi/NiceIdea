<template>
  <div>
    <Header />
    <v-container>
      <v-card class="mx-auto mb-2">
        <v-card-text>
          <h2>
            <v-icon style="font-size: 18px; color: #4caf50">{{
              svgPerson
            }}</v-icon
            >【{{ idea.title }}】
          </h2>
          <p>{{ idea.content }}</p>
        </v-card-text>
        <v-card-actions>
          <newComment :id="this.id" />
        </v-card-actions>
      </v-card>
      <comment
        v-for="(comment, key) in idea.comments"
        :key="key"
        :comment="comment"
      ></comment>
    </v-container>
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Comment from "@/components/Comment";
import newComment from "@/components/newComment";
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
    Comment,
    newComment,
  },
  data() {
    return {
      idea: {},
      comments: {},
      svgPerson: "mdi-head-lightbulb-outline",
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
        .then(() => this.setPageTitle(this.idea.title))
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
    // getCommentData() {
    //   axios
    //     .get(`/api/comments/${this.id}/`, {
    //       headers: { Authorization: "JWT " + localStorage.getItem("token") },
    //     })
    //     .then((response) => (this.comments = response.data))
    //     .catch((error) => {
    //       console.log(error);
    //       this.$swal({
    //         type: "warning",
    //         title: "ログイン",
    //         text: "再ログインしてください",
    //         showConfirmButton: false,
    //         showCloseButton: false,
    //         timer: 1000,
    //       });
    //       this.$router.push("/login");
    //     });
    // },
    // deleteIdeaData() {
    //   axios
    //     .delete(`/api/ideas/${this.id}/`, {
    //       headers: { Authorization: "JWT " + localStorage.getItem("token") },
    //     })
    //     .then(() =>
    //       this.$router.push({
    //         name: "home",
    //       })
    //     )
    //     .catch((error) => {
    //       console.log(error);
    //       this.$swal({
    //         type: "warning",
    //         title: "ログイン",
    //         text: "再ログインしてください",
    //         showConfirmButton: false,
    //         showCloseButton: false,
    //         timer: 1000,
    //       });
    //       this.$router.push("/login");
    //     });
    // },
  },
  created() {
    this.getIdeaData();
  },
};
</script>

<style>
newComment {
  position: absolute;
  bottom: 30px;
}
</style>