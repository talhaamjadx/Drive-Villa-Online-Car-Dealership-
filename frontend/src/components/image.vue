<template>
  <div>
    <v-img :src="image" height="200" width="200"></v-img>
    <v-col cols="6" class="">
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
    <p class="mt-2 caption" style="color: red">
      (Click the attach icon to change the image!)
    </p>
    <v-btn
      style="position: absolute; margin-top: -85px; margin-left: 60px; pointer-events: none"
      v-if="check"
      rounded
      small
      tag="p"
      depressed
      >{{ selectedFile.name }}</v-btn
    >
    <!-- <button @click="remove" class="btn btn-sm btn-danger ml-2">Delete</button> -->
  </div>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";

export default {
  props: ["imgID", "adID"],
  data: function() {
    return {
      image: "",
      selectedFile: null,
      check: false,
    };
  },
  methods: {
    async onFileSelected(event) {
      this.selectedFile = event.target.files[0];
      this.check = true;
      this.$emit("gibberish", this.upload);
    },
    async upload() {
      const fd = new FormData();
      fd.append("image", this.selectedFile, this.selectedFile.name);
      axios
        .put(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adID.toString() +
            "/images/" +
            this.imgID +
            "/",
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
    async remove() {
      axios
        .delete(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adID.toString() +
            "/images/" +
            this.imgID +
            "/",
          {
            headers: {
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => console.log(res))
        .catch((error) => console.log(error));
    },
    async getImages() {
      axios
        .get(
          "http://127.0.0.1:8000/api/advertisements/" +
            this.adID.toString() +
            "/images/" +
            this.imgID,
          {
            headers: {
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          this.image = res.data.image;
          console.log(this.image);
        })
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.getImages();
    console.log("started images component!");
  },
};
</script>

<style scoped></style>
