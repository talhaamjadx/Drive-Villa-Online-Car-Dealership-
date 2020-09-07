<template>
  <v-container fluid>
    <div v-if="check">
      <v-row>
        <v-col cols="1">
          <v-avatar size="40" color="red">
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
      <v-btn @click="check1 = !check1" icon class="ml-3 mt-n6">
        <v-icon>reply</v-icon>
        <p>Reply!</p>
      </v-btn>
      <div
        v-if="publisher == username"
        style="margin-left: 70px; margin-top: -45px"
      >
        <v-btn @click="check = !check" icon>
          <v-icon>create</v-icon>
        </v-btn>
        <v-btn @click="remove" icon>
          <v-icon>delete_sweep</v-icon>
        </v-btn>
      </div>
    </div>
    <div v-else>
      <v-col cols="3">
        <v-text-field v-model="q_content" outlined dense></v-text-field>
        <button @click="update" class="btn btn-sm btn-secondary">
          Update!
        </button>
      </v-col>
    </div>
    <br />
    <v-divider />
    <ans-comp
      :key="$store.state.answer_count"
      :check1="check1"
      :questionSlug="questionSlug"
      :adId="adId"
    ></ans-comp>
  </v-container>
</template>

<script>
import Answers from "./answers";
import { csrftoken } from ".././assets/csrf";
import axios from "axios";
import { mapMutations } from "vuex";

export default {
  name: "Question",
  props: ["content", "publisher", "questionSlug", "adId"],
  components: {
    "ans-comp": Answers,
  },
  data: function() {
    return {
      check: true,
      check1: true,
      username: "",
      q_content: this.content,
    };
  },
  methods: {
    ...mapMutations(["decrement"]),
    async remove() {
      axios
        .delete(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adId +
            "/questions/" +
            this.questionSlug,
          {
            headers: {
              // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc'
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res);
          alert("Deleted!");
          // this.$router.go({ name: 'SelectAd' })
          this.decrement();
        })
        .catch((error) => console.log(error));
    },
    async update() {
      const q_data = {
        content: this.q_content,
      };
      axios
        .put(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adId +
            "/questions/" +
            this.questionSlug +
            "/",
          q_data,
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
          // this.content = this.q_content
          this.content = this.q_content;
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
