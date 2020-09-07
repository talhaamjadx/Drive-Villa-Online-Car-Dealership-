<template>
  <v-container fluid class="mt-5">
    <v-card dense>
      <v-container fluid>
        <h1 class="display-1 ml-5">Questions</h1>
      </v-container>
      <v-row v-for="res in results" :key="res.slug">
        <v-col cols="12">
          <v-container fluid class="mt-n6">
            <v-card outlined dense>
              <question-comp
                :content="res.content"
                :publisher="res.publisher"
                :questionSlug="res.slug"
                :adId="adId"
              ></question-comp>
            </v-card>
          </v-container>
        </v-col>
      </v-row>
      <v-container fluid>
        <strong><p class="ml-5">Share your thoughts!</p></strong>
        <v-textarea
          placeholder="Add a comment!"
          v-model="new_question"
          outlined
          dense
        ></v-textarea>
        <v-btn ref="postbtn" @click="post" class="primary" tile>
          Post!
        </v-btn>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";
import Question from "./question";
import { mapMutations } from "vuex";

export default {
  name: "Questions",
  props: ["adId"],
  components: {
    // 'ans-comp': Answers
    "question-comp": Question,
  },
  data: function() {
    return {
      results: [],
      new_question: "",
    };
  },
  created() {
    this.getQuestions();
  },
  methods: {
    ...mapMutations(["increment"]),
    async post() {
      const ad_data = {
        content: this.new_question,
      };
      axios
        .post(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adId +
            "/questions/",
          ad_data,
          {
            headers: {
              // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc'
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res);
          this.increment();
        })
        .catch((error) => {
          console.log(error);
          alert("please login to continue!");
          window.open("http://127.0.0.1:8000/accounts/login/", "_self");
        });
    },
    async getQuestions() {
      axios
        .get(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adId +
            "/questions/",
          {
            headers: {
              // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc'
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          this.results = res.data;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style scoped></style>
