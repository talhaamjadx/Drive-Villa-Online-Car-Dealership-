<template>
  <v-container fluid>
    <v-card class="d-flex flex-column">
      <v-row>
        <v-col cols="1" class="ml-5">
          <h1 class="title">Name:</h1>
        </v-col>
        <v-col cols="10">
          <h1 class="title ml-8">
            {{ details.first_name }} {{ details.last_name }}
          </h1>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2" class="ml-5">
          <h1 class="title">Username:</h1>
        </v-col>
        <v-col cols="9">
          <h1 class="title" style="margin-left: -78px">
            {{ details.username }}
          </h1>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="1" class="ml-5">
          <h1 class="title">Email:</h1>
        </v-col>
        <v-col cols="10">
          <h1 class="title ml-8">{{ details.email }}</h1>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="1" class="ml-5">
          <h1 class="title">CNIC:</h1>
        </v-col>
        <v-col cols="10">
          <h1 class="title ml-8">{{ details.customer_cnic }}</h1>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2" class="ml-5">
          <h1 class="title">Date of Birth:</h1>
        </v-col>
        <v-col cols="9">
          <h1 class="title" style="margin-left: -78px">
            {{ details.customer_dob }}
          </h1>
        </v-col>
      </v-row>
    </v-card>
    <v-card min-height="300" class="mt-5 blue-grey lighten-5" outlined>
      <v-row>
        <h1 class="display-1 ml-10 mt-3">Advertisements</h1>
      </v-row>
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
              <v-card-text
                class="font-weight-bold headline d-flex justify-center"
                >Posted By: {{ res.seller_name }}</v-card-text
              >
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";
import Image from "./adimage";

export default {
  name: "Seller",
  components: {
    "image-comp": Image,
  },
  data() {
    return {
      seller_id: this.$route.params.seller_id,
      result: [],
      details: {},
    };
  },
  methods: {
    getUser() {
      axios
        .get(
          "http://127.0.0.1:8000/api/advertisements/seller/" + this.seller_id,
          {
            headers: {
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          this.result = res.data;
        })
        .catch((error) => console.log(error));
    },
    getUserDetails() {
      axios
        .get("http://127.0.0.1:8000/api/custom-users/" + this.seller_id, {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          console.log(res.data);
          this.details = res.data;
        })
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.getUser();
    this.getUserDetails();
  },
};
</script>
