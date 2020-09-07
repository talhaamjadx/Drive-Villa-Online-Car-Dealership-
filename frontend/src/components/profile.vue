<template>
  <v-container fluid style="height: 100vh">
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
      <v-col>
        <v-btn
          tile
          depressed
          style="text-decoration:none"
          class="secondary"
          :to="{ name: 'EditProfile' }"
          >Edit!</v-btn
        >
      </v-col>
    </v-card>
    <h1 class="headline mt-6">Your Advertisements!</h1>
    <v-btn
      :to="{ name: 'AdList' }"
      style="text-decoration: none"
      class="primary"
    >
      Advertisements
    </v-btn>
  </v-container>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";

export default {
  name: "Profile",
  data() {
    return {
      username: "",
      details: {},
    };
  },
  methods: {
    getUserDetails() {
      axios
        .get("http://127.0.0.1:8000/api/current-user/", {
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
    this.getUserDetails();
  },
};
</script>
