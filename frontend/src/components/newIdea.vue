<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="success"
          dark
          fab
          v-bind="attrs"
          v-on="on"
          class="ideabutton"
        >
          <v-icon style="font-size: 32px">{{ svgPath }}</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-form>
          <v-toolbar dark color="success">
            <v-btn text dark @click="dialog = false"> キャンセル </v-btn>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark text @click="onSubmit" :disabled="content == ''">
                投稿する
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-textarea
            v-model="content"
            placeholder="アイデアを思い付いたら気軽に投稿しましょう！"
            counter
            maxlength="255"
            color="success"
            required
            class="ideacontents"
          >
          </v-textarea>
        </v-form>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      dialog: false,
      notifications: false,
      sound: true,
      widgets: false,
      svgPath: "mdi-lightbulb-on-outline",
      content: "",
    };
  },
  methods: {
    onSubmit() {
      const datas = {
        content: this.content,
      };
      axios
        .post("/api/ideas/", datas, {
          headers: {
            Authorization: "JWT " + localStorage.getItem("token"),
          },
        })
        .then((response) => {
          console.log(response.data);
          // this.$router.go({
          //   path: this.$router.currentRoute.path,
          //   force: true,
          // });
        })
        .catch((error) => {
          console.log(error);
          // this.$swal({
          //   type: "warning",
          //   title: "ログイン",
          //   text: "再ログインしてください",
          //   showConfirmButton: false,
          //   showCloseButton: false,
          //   timer: 1000,
          // });
          // this.$router.push("/login");
        });
    },
  },
};
</script>

<style scoped>
.ideabutton {
  position: fixed;
  right: 20px;
  bottom: 50px;
}

.ideacontents {
  padding: 10px;
}
</style>