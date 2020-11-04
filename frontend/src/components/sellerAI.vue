<template>
  <div class="container">
    <h1>Hello from seller AI</h1>
    <input type="text" v-model="message" /><br /><br />
    <v-btn @click="sendMessage()">Submit</v-btn>
    <h1>Responses:</h1>
    <p v-for="res in response" :key="res">{{ res }}</p>
  </div>
</template>

<script>
import { csrftoken } from ".././assets/csrf";
import axios from "axios";

export default {
  name: "SellerAI",
  data: function() {
    return {
      message: "",
      response: [],
      seller_name: this.$route.params.seller_name,
    };
  },
  methods: {
    sendMessage() {
      const dataObject = {
        message: this.message,
      };
      axios
        .post(
          "http://127.0.0.1:8000/api/chatbot/" + this.seller_name + "/",
          dataObject,
          {
            headers: {
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          this.response.push(res.data.response);
          this.getMessages();
        });
    },
    getMessages() {
      axios
        .get("http://127.0.0.1:8000/api/chatbot/" + this.seller_name, {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          console.log(res.data);
        });
    },
  },
};
</script>

<style scoped>
div {
  height: 100vh;
}
input {
  border: 2px solid black;
}
</style>
