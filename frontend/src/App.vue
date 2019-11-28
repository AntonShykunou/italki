<template>
  <div id="app">
    <navbar/>
    <teachercards/>
    <login/>
  </div>
</template>

<script>
import navbar from "./components/navbar"
import teachercards from "./components/teachercards"
import login from "@/views/Login";
export default {
  name: "app",
  components: {
    navbar, teachercards, login
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

#app{
  background: grey;
}
</style>
