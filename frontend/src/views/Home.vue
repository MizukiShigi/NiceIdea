<template>
  <div>
    <Header />
    <v-container>
      <h2>Idea Board</h2>
      <div v-for="idea in ideas" :key="idea.pk">
        <h3>
          <router-link
            :to="{ name: 'idea', params: { id: idea.id } }"
            class="idea-link"
            >{{ idea.company_name }}
          </router-link>
        </h3>
        <p>{{ idea.idea_title }}</p>
        <hr />
      </div>
      <div class="my-4">
        <p v-show="loadingIdeas">...loading...</p>
        <v-btn v-show="next" @click="getIdeas" color="success">Load More</v-btn>
      </div>
    </v-container>
    <NewIdea />
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import NewIdea from "@/components/newIdea";

export default {
  name: "home",
  components: {
    Header,
    Footer,
    NewIdea,
  },
  data() {
    return {
      ideas: [],
      next: null,
      loadingIdeas: false,
    };
  },
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      const token = localStorage.getItem("token");
      console.log(token);
      if (token === null) {
        this.$router.push("/login");
      }
    },
    getIdeas() {
      this.checkLoggedIn();
      const endpoint = this.next ? this.next : "api/ideas/";
      this.loadingIdeas = true;
      axios
        .get(endpoint, {
          headers: {
            Authorization: "JWT " + localStorage.getItem("token"),
          },
        })
        .then((response) => {
          console.log(response.data);
          this.ideas.push(...response.data.results);
          this.loadingIdeas = false;
          if (response.data.next) {
            this.next = response.data.next;
          } else {
            this.next = null;
          }
        })
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
    this.getIdeas();
    console.log(this.ideas);
    document.title = "Idea Board";
  },
};
</script>

<style scoped>
h2 {
  color: #4caf50;
}
.idea-link {
  font-weight: bold;
  color: black;
  text-decoration: none;
}

.idea-link:hover {
  color: #4caf50;
}
</style>