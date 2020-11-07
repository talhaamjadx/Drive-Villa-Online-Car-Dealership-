<template>
  <div>
    <v-img
      v-for="res in results"
      :key="res.id"
      :src="res.image"
      max-height="200"
      class="d-flex align-end"
    >
      <v-card dark style="background: rgba(0,0,0,0.5)">
        <v-card-title style="color: white;">{{ title }}</v-card-title>
      </v-card>
    </v-img>
  </div>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";

export default {
  props: ["adId", "title"],
  data() {
    return {
      results: [],
    };
  },
  methods: {
    getImage() {
      axios
        .get(
          "http://127.0.0.1:8000/api/advertisements/" + this.adId + "/images/",
          {
            headers: {
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          this.results = res.data;
          console.log("image", this.results)
          this.$store.state.ad_image.push(res.data[0].image);
        })
        .catch((error) => console.log(error));
    },
  },
  async mounted() {
    await this.getImage();
  },
};
</script>

<style scoped></style>
