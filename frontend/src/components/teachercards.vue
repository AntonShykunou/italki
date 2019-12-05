<template>
  <div class="teachercontainer">
    <h1>
      Более 10 000 преподавателей.
      <span style="color: red;">Любой язык.</span>
    </h1>
    <carousel>
      <slide><a href=""><img src="../assets/1.png" alt=""></a></slide>
      <slide><a href=""><img src="../assets/1.png" alt=""></a></slide>
      <slide><a href=""><img src="../assets/1.png" alt=""></a></slide>
      <slide><a href=""><img src="../assets/1.png" alt=""></a></slide>
    </carousel>
  </div>
</template>
<script>
import { Carousel, Slide } from "vue-carousel";
export default {
  components: {
    Carousel,
    Slide
  }
};
</script>

<style>
.teachercontainer {
  overflow: hidden;
  display: block;
  text-align: center;
  min-width: 960px;
  padding-left: 1rem;
  padding-right: 1rem;
  margin-top: 15px;
  border: 1px solid red;
  align-content: center;
  display: flexbox;
}
.cont-wth-cards {
  display: flexbox;
  width: 900px;
  height: 400px;
}
.card {
  max-height: 200px;
  max-width: 300px;
}
</style>