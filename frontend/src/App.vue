<template>
  <div id="app" style="height: 100vh">
    <v-app>
    <NavBar></NavBar>
      <router-view/>
    <Footer></Footer>
    </v-app>
  </div>
</template>

<script>
import NavBar from './components/navbar'
import Footer from './components/footer'

export default {
  data: function(){
    return{
      
    }
  },
  created(){

  },
  components:{
    NavBar,
    Footer,
  },
}
</script>

<style scoped>
</style>
