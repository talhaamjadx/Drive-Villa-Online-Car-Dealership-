<template>
  <v-container fluid>
    <h1 class="mb-2">Advertisements</h1>
    <v-container>
      <v-row>
        <v-col cols="6" v-for="res in result" :key="res.ad_id">
          <v-card
            hover
            :to="{ name: 'SelectAd', params: { id: res.ad_id } }"
            style="text-decoration:none"
            ripple
          >
            <image-comp :adId="res.ad_id" :title="res.title"></image-comp>
            <v-card-text>Description: {{ res.description }}</v-card-text>
            <v-card-text>Expected Price: {{ res.expected_price }}</v-card-text>
            <v-card-text class="font-weight-bold"
              >Posted By: {{ res.seller_name }}</v-card-text
            >
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import axios from "axios";
import { csrftoken } from "../assets/csrf";
import Image from "./adimage";

export default {
  name: "Advertisement",
  data: function() {
    return {
      result: [],
    };
  },
  components: {
    "image-comp": Image,
  },
  async mounted() {
    await this.getApiData();
  },
  methods: {
    getApiData() {
      axios
        .get("http://127.0.0.1:8000/api/advertisements/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
            // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc',
          },
        })
        .then((res) => {
          this.result = res.data;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style scoped>
a {
  cursor: pointer;
}
</style>
