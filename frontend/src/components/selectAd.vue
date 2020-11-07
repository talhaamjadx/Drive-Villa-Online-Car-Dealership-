/* eslint-disable */
<template>
  <v-container fluid style="background-color: #ededed">
    <v-card>
      <v-row>
        <v-col cols="6" v-for="image in images" :key="image.id" class="ml-4">
          <v-card outlined class="d-flex justify-center align-center ml-7 mt-6">
            <v-img :src="image.image" height="400" width="700"></v-img>
          </v-card>
          <div v-if="results.seller_name == username">
            <v-btn class="primary ml-10 mt-4" tile @click="edit">Edit!</v-btn>
            <v-btn class="error ml-3 mt-4" tile @click="remove">Delete!</v-btn>
          </div>
        </v-col>
        <v-col cols="5" class="mt-6">
          <v-card class="ml-12" outlined width="800">
            <h1 class="display-1 mt-2 ml-3 font-weight-bold">
              {{ results.title }}
            </h1>
            <v-row>
              <v-col cols="12">
                <h1 class="display-1 ml-5" style="color: #ff5f2e">
                  Rs. {{ results.expected_price }}
                </h1>
              </v-col>
            </v-row>
            <h1 class="headline ml-5">Description:</h1>
            <h1 class="subtitle-1 ml-10">{{ results.description }}</h1>
            <v-divider />
            <h1 class="title ml-5">Seller Description</h1>
            <v-row>
              <v-col cols="1" class="mt-n3">
                <v-btn icon dark onclick="this.blur()" class="ml-5 mb-4">
                  <v-avatar size="40" color="red">
                    <span class="white--text headline">{{
                      seller_avatar_name
                    }}</span>
                  </v-avatar>
                </v-btn>
              </v-col>
              <v-col cols="10" class="mt-n2 ml-5">
                <p>{{ results.seller_name }}</p>
              </v-col>
            </v-row>
            <v-col class="d-flex justify-center mt-n5">
              <v-btn
                class="amber green--text text--accent-4"
                @click="toSeller(results.seller)"
                depressed
                tile
                >Go to Seller's Profile</v-btn
              >
            </v-col>
            <v-col class="d-flex justify-center">
              <v-btn
                v-if="results.seller_name != null"
                style="text-decoration: none"
                :to="{
                  name: 'Chat',
                  params: { username: results.seller_name },
                }"
                tile
                depressed
                color="primary"
              >
                Contact Seller
              </v-btn>
            </v-col>
            <v-col class="d-flex justify-center">
              <v-btn
                class=""
                style="text-decoration:none"
                color="secondary"
                v-if="results.seller_name"
              >
                <router-link
                  style="text-decoration:none; color:white"
                  :to="{ name: 'SellerAI', params: { seller_name: results.seller_name } }"
                  >Seller AI</router-link
                >
              </v-btn>
            </v-col>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
    <questions-comp
      :key="$store.state.question_count"
      :adId="id"
    ></questions-comp>
    <v-divider />
  </v-container>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";
import Questions from "./questions";

export default {
  name: "SelectAd",
  components: {
    "questions-comp": Questions,
  },
  data: function() {
    return {
      id: this.$route.params.id,
      results: [],
      check: false,
      username: "",
      images: [],
      selectedFile: null,
      seller_avatar_name: "",
    };
  },
  watch: {
    $route: function(to) {
      this.id = to.params.id;
    },
  },
  methods: {
    getApiData() {
      return axios
        .get("http://127.0.0.1:8000/api/advertisements/" + this.id.toString(), {
          headers: {
            // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc',
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          this.results = res.data;
          this.seller_avatar_name = res.data.seller_name
            .substring(0, 2)
            .toUpperCase();
          console.log(res.data);
        })
        .catch((error) => console.log(error));
    },

    remove() {
      return axios
        .delete(
          "http://127.0.0.1:8000/api/advertisements/" + this.id.toString(),
          {
            headers: {
              // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc',
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res);
          this.$router.push("/");
        })
        .catch((error) => console.log(error));
    },

    edit() {
      this.$router.push({ name: "EditAd" });
    },
    getUser() {
      return axios
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
    getImages() {
      return axios
        .get(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.id.toString() +
            "/images/",
          {
            headers: {
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          this.images = res.data;
          console.log("this.images", this.images)
        })
        .catch((error) => console.log(error));
    },
    toSeller(seller_id) {
      this.$router.push({ name: "Seller", params: { seller_id: seller_id } });
    },
  },
  async mounted() {
    await this.getApiData();
    await this.getImages();
    await this.getUser();
  },
};
</script>

<style scoped></style>
