<template>
  <div class="container mt-5 mb-10">
    <v-container fluid class="d-flex flex-column align-center">
      <v-card height width="800" elevation="20" style="border-radius: 20px">
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
            <label>Description *</label>
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
            <label class="ml-5">Expected Price *</label>
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
            <label class="ml-3">Add a Vehicle *</label>
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
        <v-row>
          <v-col cols="4" class="d-flex justify-center align-center">
            <label class="ml-3">Add an Image *</label>
          </v-col>
          <v-col cols="6" class="mb-2">
            <input
              type="file"
              @change="onFileSelected"
              style="display:none"
              ref="fileUpload"
            />
            <v-btn icon @click="$refs.fileUpload.click()">
              <v-icon large>attach_file</v-icon>
            </v-btn>
          </v-col>
        </v-row>
        <v-btn
          style="position: absolute; margin-top: -50px; margin-left: 350px; pointer-events: none"
          v-if="check"
          rounded
          small
          tag="p"
          depressed
          >{{ selectedFile.name }}</v-btn
        >
        <br />
        <v-col cols="12" class="d-flex justify-center mb-10">
          <v-btn @click="post" tile width="200" color="#002354" dark x-large
            >Post!</v-btn
          >
        </v-col>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
// import hello from '.././assets/hello'
import { csrftoken } from ".././assets/csrf";

export default {
  name: "Post",
  data: function() {
    return {
      title: "",
      description: "",
      exp_price: "",
      v_id: "",
      choice: "",
      v_data: [],
      ad_id: "",
      selectedFile: null,
      check: false,
    };
  },
  methods: {
    async upload() {
      const fd = new FormData();
      fd.append("image", this.selectedFile, this.selectedFile.name);
      axios
        .post(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.ad_id.toString() +
            "/images/",
          fd,
          {
            headers: {
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res);
        })
        .catch((error) => console.log(error));
    },
    async onFileSelected(event) {
      this.selectedFile = event.target.files[0];
      this.check = true;
    },
    async post() {
      const adData = {
        title: this.title,
        description: this.description,
        expected_price: this.exp_price,
        vehicle_id: this.choice,
      };
      axios
        .post("http://127.0.0.1:8000/api/advertisements/", adData, {
          headers: {
            "X-CSRFTOKEN": csrftoken,
            // 'Authorization' : 'Token 5be274af6d7e24741e747d359ed910eda61a86fc',
          },
        })
        .then((res) => {
          console.log(res);
          this.ad_id = res.data.ad_id;
          this.upload();
          this.$router.replace({
            name: "SelectAd",
            params: { id: this.ad_id },
          });
        })
        .catch((error) => {
          console.log(error);
          alert("Please Login To Continue!");
          window.open("http://127.0.0.1:8000/accounts/login/", "_blank");
        });
    },
    async getVehicles() {
      axios
        .get("http://127.0.0.1:8000/api/vehicles/", {
          headers: {
            // 'Authorization' : 'Token 5be274af6d7e24741e747d359ed910eda61a86fc',
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          this.v_data = res.data;
          console.log(res.data);
        })
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.getVehicles();
  },
};
</script>

<style scoped></style>
