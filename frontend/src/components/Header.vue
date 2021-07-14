<template>
  <div>
    <v-app-bar color="success" dark app>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-toolbar-title style="font-size: 24px"
        ><v-icon color="#FBC02D" style="font-size: 20px">{{ svgPath }}</v-icon
        >NiceIdea</v-toolbar-title
      >
      <v-spacer></v-spacer>
      <!-- <v-toolbar-items>
        <v-btn text to="/">ホーム</v-btn>
        <v-btn text to="/editer">投稿</v-btn>
        <v-btn text to="/login">ログアウト</v-btn>
      </v-toolbar-items> -->
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" fixed temporary>
      <v-list nav dense>
        <v-list-item-group>
          <v-list-item to="/">
            <v-list-item-title>ホーム</v-list-item-title>
          </v-list-item>
          <v-list-item to="/editer">
            <v-list-item-title>投稿</v-list-item-title>
          </v-list-item>
          <v-list-item to="/login">
            <v-list-item-title>ログアウト</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      svgPath: "mdi-lightbulb-on-outline",
    };
  },
};
</script>