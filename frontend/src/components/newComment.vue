<template>
  <v-card>
    <v-form>
      <v-text-field
        label="コメント"
        placeholder="アイデアのブラッシュアップのためにコメントをしましょう！"
        counter
        maxlength="100"
        color="success"
        required
        outlined
        class="ideatitle"
      ></v-text-field>
    </v-form>
  </v-card>
</template>

<script>
import axios from "axios";
export default {
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      content: "",
    };
  },
  methods: {
    onSubmit() {
      const datas = {
        content: this.content,
      };
      axios
        .post(`/api/comments/${this.id}`, datas, {
          headers: {
            Authorization: "JWT " + localStorage.getItem("token"),
          },
        })
        .then((response) => {
          console.log(response.data);
          this.$router.go({
            path: this.$router.currentRoute.path,
            force: true,
          });
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
};
</script>

<style scoped>
.ideabutton {
  position: fixed;
  right: 20px;
  bottom: 60px;
}

.ideacontents {
  padding: 10px;
}

.ideatitle {
  padding: 10px;
  line-height: 1.5rem;
}
</style>