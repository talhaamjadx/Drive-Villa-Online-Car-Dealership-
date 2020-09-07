<template>
  <v-card color="grey lighten-4" flat height="70px" tile>
    <v-toolbar dense>
      <v-toolbar-title>Drive Villa</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text class="mr-2" to="/" style="text-decoration:none" outlined>
        <router-link style="text-decoration:none" :to="{ name: 'Home' }"
          >Home</router-link
        >
      </v-btn>

      <v-btn text class="mr-2" to="/post" style="text-decoration:none" outlined>
        <router-link style="text-decoration:none" to="/post"
          >Post an Ad!</router-link
        >
      </v-btn>
      <v-btn
        text
        class="mr-2"
        to="/advertisements"
        style="text-decoration:none"
        outlined
      >
        <router-link
          style="text-decoration:none"
          :to="{ name: 'Advertisement' }"
          >Advertisements</router-link
        >
      </v-btn>

      <v-btn
        v-if="!check"
        text
        class="mr-2"
        to="/chat"
        style="text-decoration:none"
        outlined
      >
        <router-link style="text-decoration:none" :to="{ name: 'Messages' }"
          >Messages</router-link
        >
      </v-btn>
      <v-btn
        v-if="check"
        href="/accounts/login/"
        style="text-decoration:none"
        color="primary"
        raised
      >
        Login
      </v-btn>

      <v-btn icon x-large v-else>
        <v-icon>shopping_cart</v-icon>
      </v-btn>

      <v-menu
        id="menu"
        v-if="!check"
        offset-y
        origin="center center"
        transition="scale-transition"
        min-width="200"
      >
        <template v-slot:activator="{ on }">
          <v-btn icon dark v-on="on" onclick="this.blur()">
            <v-avatar size="40" color="red">
              <span class="white--text headline">{{
                username.substring(0, 2).toUpperCase()
              }}</span>
            </v-avatar>
          </v-btn>
        </template>

        <v-list dense nav>
          <v-list-item>
            <v-list-item-title class="mt-2 ml-3"
              >Welcome {{ username.toUpperCase() }}!</v-list-item-title
            >
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item>
            <v-icon class="mr-3">account_box</v-icon>
            <router-link
              class="link1"
              :to="{ name: 'Profile' }"
              style="text-decoration: none;"
              >Your Profile</router-link
            >
          </v-list-item>
          <v-list-item>
            <v-icon class="mr-3">mdi-folder</v-icon>
            <router-link
              class="link1"
              :to="{ name: 'AdList' }"
              style="text-decoration: none"
              >Advertisements</router-link
            >
          </v-list-item>
          <v-list-item>
            <v-icon class="mr-3">build</v-icon>
            <router-link
              class="link1"
              :to="{ name: 'Setting' }"
              style="text-decoration:none"
              >Settings</router-link
            >
          </v-list-item>
          <v-divider />
          <v-list-item>
            <v-btn
              class="mb-2 ml-10"
              href="/accounts/logout/"
              style="text-decoration:none"
              color="error"
            >
              Logout
            </v-btn>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-toolbar>
  </v-card>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";
export default {
  data: function() {
    return {
      check: true,
      username: "",
      colors: "primary",
    };
  },
  methods: {
    async getUser() {
      axios
        .get("http://127.0.0.1:8000/api/user/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          console.log(res);
          if (res.data.username != "") {
            this.username = res.data.username;
            this.check = false;
          }
        })
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.getUser();
  },
};
</script>

<style scoped>
.link1 {
  color: black;
}

.link1:hover {
  color: red;
}
</style>
