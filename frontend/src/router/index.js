import Vue from "vue";
import VueRouter from "vue-router";
import Post from ".././components/post.vue";
import Advertisement from ".././components/advertisement.vue";
import SelectAd from ".././components/selectAd";
import EditAd from ".././components/editAd";
import Profile from "../components/profile";
import AdList from ".././components/adList";
import Setting from ".././components/settings";
import Home from ".././components/home";
import Seller from ".././components/seller";
import EditProfile from ".././components/editProfile";
import Chat from ".././components/chat";
import Message from ".././components/message";

Vue.use(VueRouter);

const routes = [
  {
    path: "/advertisements",
    name: "Advertisement",
    component: Advertisement,
  },
  {
    path: "/post",
    name: "Post",
    component: Post,
  },
  {
    path: "/select-ad/:id",
    name: "SelectAd",
    component: SelectAd,
  },
  {
    path: "/edit-ad/:id",
    name: "EditAd",
    component: EditAd,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/adlist",
    name: "AdList",
    component: AdList,
  },
  {
    path: "/settings",
    name: "Setting",
    component: Setting,
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/seller/:seller_id",
    name: "Seller",
    component: Seller,
    props: true,
  },
  {
    path: "/edit-profile",
    name: "EditProfile",
    component: EditProfile,
  },
  {
    path: "/chat/:username",
    name: "Chat",
    component: Chat,
  },
  {
    path: "/chat",
    name: "Messages",
    component: Message,
  },
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes,
});

export default router;
