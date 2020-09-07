<template>
  <div>
    <strong><p>Answers:</p></strong>
    <p v-if="check">No answers yet!</p>
    <v-row v-for="res in results" :key="res.ans_slug">
      <v-col>
        <ans-comp
          :content="res.content"
          :publisher="res.publisher"
          :adId="adId"
          :questionSlug="questionSlug"
          :ansSlug="res.ans_slug"
        ></ans-comp>
      </v-col>
      <br />
    </v-row>
    <div v-if="!check1">
      <v-container>
        <v-textarea
          placeholder="Add an answer!"
          v-model="new_ans"
          outlined
          dense
        ></v-textarea>
        <button @click="reply" class="btn btn-sm btn-primary">Reply</button>
      </v-container>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";
import Answer from "./answer";
import { mapMutations } from "vuex";

export default {
  name: "Answers",
  props: ["questionSlug", "adId", "check1"],
  components: {
    "ans-comp": Answer,
  },
  data: function() {
    return {
      results: [],
      check: false,
      new_ans: "",
      keys: 1,
    };
  },
  created() {
    this.getAnswer();
  },
  methods: {
    ...mapMutations(["ans_inc"]),
    async reply() {
      const ansData = {
        content: this.new_ans,
      };
      axios
        .post(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adId +
            "/questions/" +
            this.questionSlug +
            "/answers/",
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
          this.ans_inc();
        })
        .catch((error) => console.log(error));
    },
    async getAnswer() {
      axios
        .get(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adId +
            "/questions/" +
            this.questionSlug +
            "/answers/",
          {
            headers: {
              // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc'
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          this.results = res.data;
          console.log(res);
          if (this.results.length == 0) {
            this.check = true;
          }
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style scoped></style>
