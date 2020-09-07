<template>
  <div>
    <v-container fluid style="z-index:2; position:absolute">
      <div id="div1">
        <h1 class="mt-4">Check out our</h1>
        <h1>new arrivals</h1>
        <p class="mt-4">Amazing deals with the</p>
        <p style="margin-top:-15px">best pool of customers</p>
        <p style="margin-top:-15px">in the market.</p>
        <v-btn dark rounded elevation="5" class="mt-3">New Arrivals</v-btn>
        <v-btn outlined rounded elevation="5" color="primary" class="mt-3"
          >More Info</v-btn
        >
      </div>
      <v-container fluid class="d-flex justify-end" style="margin-top:50px">
        <v-card
          dark
          style="background: rgba(0,0,0,0); margin-right: 100px"
          width="600"
          elevation="0"
        >
          <h1 class="h11">Selling and Buying cars</h1>
          <h1 class="h11 ml-6">has never been easier</h1>
          <v-row class="mt-10">
            <v-col cols="1" class="d-flex align-self-center">
              <v-icon x-large color="#ffea29"
                >mdi-checkbox-marked-circle</v-icon
              >
            </v-col>
            <v-col cols="11">
              <h1>Customer Satisfaction</h1>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="1" class="d-flex align-self-center">
              <v-icon x-large color="#ffea29"
                >mdi-checkbox-marked-circle</v-icon
              >
            </v-col>
            <v-col cols="11">
              <h1>Hello World</h1>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="1" class="d-flex align-self-center">
              <v-icon x-large color="#ffea29"
                >mdi-checkbox-marked-circle</v-icon
              >
            </v-col>
            <v-col cols="11">
              <h1>Random text</h1>
            </v-col>
          </v-row>
        </v-card>
      </v-container>
    </v-container>
    <v-img :src="image" alt="image" height="700" style="z-index:1"></v-img>
    <div style="height: 100vh">
      <v-carousel
        continuous
        cycle
        height="100vh"
        hide-delimiter-background
        show-arrows-on-hover
        interval="5000"
      >
        <v-carousel-item>
          <div>
            <img
              src=".././assets/car1.jpg"
              alt
              style="position: absolute"
              height="100%"
              width="100%"
            />
            <h1 style="position: absolute; margin-top: 550px; color:white">
              hello
            </h1>
          </div>
        </v-carousel-item>
        <v-carousel-item>
          <div>
            <img
              src=".././assets/car2.jpg"
              alt
              style="position: absolute"
              height="100%"
              width="100%"
            />
            <h1 style="position: absolute; margin-top: 550px; color:white">
              hello
            </h1>
          </div>
        </v-carousel-item>
      </v-carousel>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapActions } from "vuex";
import { csrftoken } from ".././assets/csrf";

export default {
  name: "Home",
  data() {
    return {
      image: require("@/assets/cars.jpg"),
    };
  },
  methods: {
    ...mapActions(["get_connection2"]),
    showActive() {
      axios
        .get("http://127.0.0.1:8000/api/user/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          if (res.data.id == null) {
            console.log("anonymous user");
          } else {
            console.log("verified user");
            this.get_connection2();
          }
        });
    },
  },
  created() {
    this.showActive();
  },
};
</script>

<style scoped>
#div1 h1 {
  color: #d40202;
  font-family: "Righteous", cursive;
  font-size: 30px;
}

p {
  font-weight: bold;
}

.h11 {
  color: white;
  font-size: 50px;
  font-family: "Abril Fatface", cursive;
  /* font-style: italic; */
}

#div1 {
  z-index: 3;
  position: absolute;
  display: flex;
  flex-direction: column;
  background-color: white;
  opacity: 0.9;
  height: 350px;
  width: 300px;
  margin-left: 80px;
  margin-top: -12px;
  align-items: center;
}</style
>>
