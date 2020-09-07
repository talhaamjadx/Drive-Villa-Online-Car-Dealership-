<template>
  <v-container fluid style="height: 100vh">
    <v-row v-for="res in results" :key="res.id">
      <v-col>
        <router-link
          :to="{
            name: 'Chat',
            params: {
              username:
                res.sender_name == username
                  ? res.reciepent_name
                  : res.sender_name,
            },
          }"
        >
          {{
            res.sender_name == username ? res.reciepent_name : res.sender_name
          }}
        </router-link>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";

export default {
  name: "Message",
  data() {
    return {
      results: [],
      username: "",
      connection: null,
    };
  },
  methods: {
    getThread() {
      axios
        .get("http://127.0.0.1:8000/api/thread/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          console.log(res.data);
          this.results = res.data;
        })
        .catch((error) => console.log(error));
    },
    getUser() {
      axios
        .get("http://127.0.0.1:8000/api/user/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          this.username = res.data.username;
          console.log(this.username);
          this.connection = new WebSocket(
            "ws://127.0.0.1:8000/ws/thread/" + this.username + "/"
          );
          this.connection.onopen = (e) => {
            console.log(e);
          };
          this.connection.onmessage = (e) => {
            console.log(e.data);
            this.getThread();
          };
        })
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.getThread();
    this.getUser();
  },
};
</script>

<style scoped></style>
