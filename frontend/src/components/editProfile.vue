<template>
  <v-container fluid>
    <h1>Edit Profile</h1>
    <v-row class="d-flex">
      <v-col cols="1">
        <p>Username:</p>
      </v-col>
      <v-col cols="4">
        <v-text-field v-model="username" outlined dense></v-text-field>
      </v-col>
    </v-row>
    <v-row class="d-flex">
      <v-col cols="1">
        <p>First Name:</p>
      </v-col>
      <v-col cols="4">
        <v-text-field v-model="f_name" outlined dense></v-text-field>
      </v-col>
    </v-row>
    <v-row class="d-flex">
      <v-col cols="1">
        <p>Last Name:</p>
      </v-col>
      <v-col cols="4">
        <v-text-field v-model="l_name" outlined dense></v-text-field>
      </v-col>
    </v-row>
    <v-row class="d-flex">
      <v-col cols="1">
        <p>Email:</p>
      </v-col>
      <v-col cols="4">
        <v-text-field v-model="email" outlined dense></v-text-field>
      </v-col>
    </v-row>
    <v-row class="d-flex">
      <v-col cols="1">
        <p>CNIC:</p>
      </v-col>
      <v-col cols="4">
        <v-text-field v-model="cnic" outlined dense></v-text-field>
      </v-col>
    </v-row>
    <v-row class="d-flex">
      <v-col cols="2">
        Date Of Birth:
      </v-col>
      <v-col class="ml-n12" cols="5">
        <v-date-picker v-model="dob" landscape width="190"></v-date-picker>
      </v-col>
    </v-row>
    <v-btn class="secondary mb-10" tile depressed @click="update"
      >Update!</v-btn
    >
  </v-container>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";

export default {
  name: "EditProfile",
  data() {
    return {
      username: "",
      f_name: "",
      l_name: "",
      email: "",
      cnic: "",
      dob: "",
    };
  },
  methods: {
    update() {
      const userDetails = {
        first_name: this.f_name,
        last_name: this.l_name,
        username: this.username,
        email: this.email,
        customer_cnic: this.cnic,
        customer_dob: this.dob,
      };
      axios
        .put("http://127.0.0.1:8000/api/current-user/", userDetails, {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          console.log(res.data);
          this.$router.replace({ name: "Profile" });
        })
        .catch((error) => console.log(error));
    },
  },
  beforeRouteEnter(to, from, next) {
    next((vm) => {
      axios
        .get("http://127.0.0.1:8000/api/current-user/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          console.log(res.data);
          vm.username = res.data.username;
          vm.f_name = res.data.first_name;
          vm.l_name = res.data.last_name;
          vm.email = res.data.email;
          vm.cnic = res.data.customer_cnic;
          vm.dob = res.data.customer_dob;
        })
        .catch((error) => console.log(error));
      console.log(vm.a);
    });
  },
};
</script>
