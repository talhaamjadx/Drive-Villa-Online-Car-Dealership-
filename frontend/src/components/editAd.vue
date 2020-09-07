<template>
  <div style="">
    <v-container fluid class="d-flex flex-column align-center mb-10 mt-5">
      <v-card height width="800" elevation="20" style="border-radius: 20px">
        <v-col cols="12" class="d-flex justify-center">
          <p class="title">Edit The Details Below</p>
        </v-col>
        <v-divider class="mt-n5"></v-divider>
        <v-row class="mt-10">
          <v-col cols="4" class="d-flex justify-center align-center">
            <label class="mr-10">Title *</label>
          </v-col>
          <v-col cols="6">
            <v-text-field
              placeholder="Add an interesting title!"
              v-model="title"
              outlined
              dense
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4" class="d-flex justify-center align-center">
            <label>Description:</label>
          </v-col>
          <v-col cols="6">
            <v-text-field
              placeholder="Description"
              v-model="description"
              outlined
              dense
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4" class="d-flex justify-center align-center">
            <label class="ml-5">Expected Price:</label>
          </v-col>
          <v-col cols="6">
            <v-text-field
              placeholder="Expected Price"
              v-model="exp_price"
              outlined
              dense
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4" class="d-flex justify-center align-center">
            <label class="ml-n7">Vehicle:</label>
          </v-col>
          <v-col cols="6">
            <v-select
              :items="v_data"
              item-text="model"
              item-value="vehicle_id"
              outlined
              dense
              label="Vehicle"
              v-model="choice"
            ></v-select>
          </v-col>
        </v-row>
        <v-container class="d-flex" v-for="res in results" :key="res.id">
          <v-row>
            <v-col cols="4">
              <label style="margin-left:69px">Attached Image:</label>
            </v-col>
            <v-col cols="6">
              <image-comp
                :imgID="res.id"
                :adID="id"
                @gibberish="gibs = $event"
              ></image-comp>
            </v-col>
          </v-row>
        </v-container>
        <v-col cols="12" class="d-flex justify-center mb-8">
          <v-btn @click="edit" tile width="200" color="#002354" dark x-large
            >Update!</v-btn
          >
        </v-col>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";
import Image from ".././components/image";
export default {
  name: "EditAd",
  components: {
    "image-comp": Image,
  },
  data: function() {
    return {
      id: this.$route.params.id,
      title: "",
      description: "",
      exp_price: "",
      choice: "",
      v_data: [],
      results: [],
      gibs: null,
    };
  },
  methods: {
    async edit() {
      try {
        this.gibs();
      } catch (error) {
        console.log("no file selected!");
      }
      const adData = {
        title: this.title,
        description: this.description,
        expected_price: this.exp_price,
        vehicle_id: this.choice,
      };
      axios
        .put(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.id.toString() +
            "/",
          adData,
          {
            headers: {
              // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc'
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          this.$router.push({ name: "SelectAd", params: { id: this.id } });
        })
        .catch((error) => console.log(error));
    },
    async getVehicle() {
      axios
        .get("http://127.0.0.1:8000/api/vehicles/", {
          headers: {
            // 'Authorization' : 'Token 5be274af6d7e24741e747d359ed910eda61a86fc',
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          this.v_data = res.data;
        })
        .catch((error) => console.log(error));
    },
  },
  beforeRouteEnter(to, from, next) {
    next((vm) => {
      axios
        .get("http://127.0.0.1:8000/api/advertisements/" + vm.id.toString(), {
          headers: {
            // 'Authorization': 'Token 5be274af6d7e24741e747d359ed910eda61a86fc'
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          vm.title = res.data.title;
          vm.description = res.data.description;
          vm.exp_price = res.data.expected_price;
          vm.choice = res.data.vehicle_id;
        })
        .catch((error) => console.log(error));

      axios
        .get(
          "http://127.0.0.1:8000/api/advertisements/" +
            vm.id.toString() +
            "/images/",
          {
            headers: {
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          vm.results = res.data;
        })
        .catch((error) => console.log(error));
    });
  },
  created() {
    this.getVehicle();
  },
};
</script>

<style scoped></style>
