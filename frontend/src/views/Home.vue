<template>
  <div>
    <Header />
    <v-container>
      <div v-for="idea in ideas" :key="idea.pk" class="post">
        <v-card>
          <router-link
            :to="{ name: 'idea', params: { id: idea.id } }"
            class="idea-link"
          >
            <v-card-text>
              <h3>
                <v-icon style="font-size: 18px; color: #4caf50">
                  {{ svgPerson }}
                </v-icon>
                【{{ idea.title }}】
              </h3>
              <p>{{ idea.content }}</p>
            </v-card-text>
          </router-link>
          <v-card-actions>
            <good :idea="idea"></good>
          </v-card-actions>
        </v-card>
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
import Good from "@/components/Good";

export default {
  name: "home",
  components: {
    Header,
    Footer,
    NewIdea,
    Good,
  },
  data() {
    return {
      svgPerson: "mdi-head-lightbulb-outline",
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
          console.log(...response.data);
          if (response.data.length !== 0) {
            this.ideas.push(...response.data);
          }
          this.loadingIdeas = false;
          if (response.data.next) {
            this.next = response.data.next;
          } else {
            this.next = null;
          }
        });
      // .catch((error) => {
      //   console.log(error);
      //   this.$swal({
      //     type: "warning",
      //     title: "ログイン",
      //     text: "再ログインしてください",
      //     showConfirmButton: false,
      //     showCloseButton: false,
      //     timer: 1000,
      //   });
      //   this.$router.push("/login");
      // });
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
h3 {
  font-weight: bold;
}
.idea-link {
  text-decoration: none;
  color: black;
}

.idea-link:hover {
  color: #4caf50;
}

.post {
  padding-top: 8px;
}
</style>