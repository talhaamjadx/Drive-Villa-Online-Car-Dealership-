<template>
  <v-container fluid style="height: 100vh">
    <h1>Your Advertisements!</h1>
    <v-row class="d-flex justify-center">
      <v-col cols="11" v-for="res in result" :key="res.ad_id">
        <v-card
          class="d-flex"
          :to="{ name: 'SelectAd', params: { id: res.ad_id } }"
          style="text-decoration: none"
          hover
          ripple
        >
          <v-card width="320" height="200">
            <image-comp :adId="res.ad_id" :title="res.title"></image-comp>
          </v-card>
          <v-row>
            <v-card-text class="headline d-flex justify-center">
              {{ res.title }}
            </v-card-text>
            <v-card-text class="headline d-flex justify-center"
              >Expected Price: {{ res.expected_price }}</v-card-text
            >
            <v-card-text class="font-weight-bold headline d-flex justify-center"
              >Posted By: {{ res.seller_name }}</v-card-text
            >
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";
import Image from "./adimage";

export default {
  name: "AdList",
  components: {
    "image-comp": Image,
  },
  data() {
    return {
      result: [],
    };
  },
  methods: {
    async getAdList() {
      axios
        .get("http://127.0.0.1:8000/api/adlist/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          this.result = res.data;
          console.log(this.result);
        })
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.getAdList();
  },
};
</script>
