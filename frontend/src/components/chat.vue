<template>
  <v-container fluid>
    <v-row>
      <v-col class="d-flex justify-center" cols="12">
        <v-avatar size="40" color="red">
          <span class="white--text headline">{{
            reciepent.substring(0, 2).toUpperCase()
          }}</span>
        </v-avatar>
      </v-col>
      <v-col cols="12" class="d-flex justify-center mt-n5">
        {{ reciepent }}
      </v-col>
      <v-col cols="12" class="d-flex justify-center mt-n5">
        {{ status }}
      </v-col>
    </v-row>
    <v-card outlined>
      <v-container
        fluid
        ref="container"
        style="height: 55vh"
        class="overflow-y-auto"
      >
        <v-row v-for="message in messages" :key="message.id">
          <v-col>
            <v-row
              style="margin-left:10px"
              :class="{ ifSender: message.sender_name == username }"
            >
              <v-avatar
                size="40"
                color="red"
                v-if="message.sender_name != username"
                class="ml-n3"
              >
                <span class="white--text headline">{{ avatar }}</span>
              </v-avatar>
              <v-card
                flat
                outlined
                style="border-radius: 50px; padding: 0px 20px 0px 20px"
                :color="message.sender_name == username ? '#198cff' : '#ededed'"
                :class="
                  message.sender_name == username
                    ? 'white--text'
                    : 'black--text ml-2'
                "
              >
                <h1 class="body-1 mt-2">{{ message.content }}</h1>
              </v-card>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    <br />
    <v-row>
      <v-col cols="6">
        <v-text-field
          v-model="input"
          autofocus
          clearable
          counter
          dense
          outlined
          rounded
          placeholder="Send a message!"
          @keyup.native.enter="transfer"
        ></v-text-field>
      </v-col>
      <v-col cols="6">
        <v-btn @click="transfer" depressed color="secondary" tile class="mt-1"
          >Send</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import { csrftoken } from ".././assets/csrf";
import { mapActions } from "vuex";

export default {
  name: "Chat",
  data() {
    return {
      input: "",
      connection: null,
      connection2: null,
      username: "",
      reciepent: this.$route.params.username,
      messages: [],
      status: "inactive",
      json_data: null,
    };
  },
  computed: {
    avatar: function() {
      return this.reciepent.substring(0, 2).toUpperCase();
    },
  },
  updated() {
    this.scrolling();
  },
  methods: {
    ...mapActions(["get_connection"]),
    scrolling() {
      this.$refs.container.scrollTop = this.$refs.container.scrollHeight;
    },
    transfer() {
      const msgData = {
        content: this.input,
      };
      axios
        .post(
          "http://127.0.0.1:8000/api/chat-message/" + this.reciepent + "/",
          msgData,
          {
            headers: {
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          this.getMessages();
          this.$store.state.connection.send(
            JSON.stringify({
              username: this.username,
              input: this.input,
              reciepent: this.reciepent,
            })
          );
        })
        .catch((error) => console.log(error)),
        (this.input = "");
    },
    getUser() {
      axios
        .get("http://127.0.0.1:8000/api/user/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          console.log(res.data);
          this.username = res.data.username;
          this.get_connection(this.reciepent);
          this.$store.state.connection.onopen = (e) => {
            console.log(e);
          };
          this.$store.state.connection.onmessage = (e) => {
            console.log(e);
            this.getMessages();
          };
          this.$store.state.connection2.onopen = (e) => {
            console.log(e);
          };
          this.$store.state.connection2.onmessage = (e) => {
            this.json_data = JSON.parse(e.data);
            if (this.json_data["user"] == this.reciepent) {
              this.status = this.json_data["status"];
            }
          };
        })
        .catch((error) => console.log(error));
      axios
        .get("http://127.0.0.1:8000/api/active/" + this.reciepent + "/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          if (res.data.length != 0) {
            this.status = "active";
          }
        })
        .catch((error) => console.log(error));
    },
    getMessages() {
      axios
        .get("http://127.0.0.1:8000/api/chat-message/" + this.reciepent + "/", {
          headers: {
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          console.log(res.data);
          this.messages = res.data;
          this.scrolling();
        })
        .catch((error) => console.log(error));
    },
    getStatus() {},
  },
  created() {
    this.getUser();
    this.getMessages();
    // this.getStatus();
  },
};
</script>

<style scoped>
.ifSender {
  display: flex;
  justify-content: flex-end;
  margin-right: 10px;
}

::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #ffffff;
  border-radius: 10px;
}

::-webkit-scrollbar-track:hover {
  background: #e7e7e7;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: rgb(182, 182, 182);
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>
