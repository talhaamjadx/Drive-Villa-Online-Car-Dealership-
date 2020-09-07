<template>
  <div class="ml-10 mt-n6">
    <v-row v-if="check">
      <v-col cols="1">
        <v-avatar size="40" color="blue" tile>
          <span class="white--text headline">{{
            publisher.substring(0, 2).toUpperCase()
          }}</span>
        </v-avatar>
      </v-col>
      <v-col cols="11">
        <p class="title ml-n10">{{ content }}</p>
      </v-col>
      <v-col cols="12">
        <p class="subtitle mt-n3">Published By: {{ publisher }}</p>
      </v-col>
    </v-row>
    <div v-if="publisher == username" class="mt-n5">
      <v-btn v-if="check" @click="check = !check" icon>
        <v-icon>edit</v-icon>
      </v-btn>
      <v-btn v-if="check" @click="remove" icon>
        <v-icon>delete_sweep</v-icon>
      </v-btn>
      <v-col v-else>
        <v-text-field v-model="content" outlined dense></v-text-field>
        <button @click="edit" class="btn btn-sm btn-secondary mt-2">
          Update!
        </button>
      </v-col>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";
import { mapMutations } from "vuex";

export default {
  name: "Answer",
  props: ["content", "publisher", "adId", "questionSlug", "ansSlug"],
  data: function() {
    return {
      check: true,
      username: "",
    };
  },
  methods: {
    ...mapMutations(["ans_dec"]),
    async edit() {
      const ansData = {
        content: this.content,
      };
      axios
        .put(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adId +
            "/questions/" +
            this.questionSlug +
            "/answers/" +
            this.ansSlug +
            "/",
          ansData,
          {
            headers: {
              // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc'
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res);
          this.check = !this.check;
        })
        .catch((error) => console.log(error));
    },
    async remove() {
      axios
        .delete(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adId +
            "/questions/" +
            this.questionSlug +
            "/answers/" +
            this.ansSlug +
            "/",
          {
            headers: {
              // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc'
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res);
          this.ans_dec();
        })
        .catch((error) => console.log(error));
    },
    async getUser() {
      axios
        .get("http://127.0.0.1:8000/api/user/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          this.username = res.data.username;
          console.log(this.username);
        })
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.getUser();
  },
};
</script>

<style scoped></style>
