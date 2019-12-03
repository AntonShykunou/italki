<template>
  <div id="app">
    <navbar/>
  </div>
</template>

<script>
import navbar from "./components/navbar"


export default {
  name: "app",
  components: {
    navbar
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

#app{
  background: grey;
}
</style>
