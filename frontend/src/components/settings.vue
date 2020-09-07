<template>
  <v-container fluid style="height: 100vh">
    <h1>Settings</h1>
    <v-btn class="secondary" @click="$router.push({ name: 'EditProfile' })"
      >Change Account Info!</v-btn
    >
  </v-container>
</template>

<script>
export default {
  name: "Setting",
};
</script>
