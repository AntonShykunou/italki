<template>
  <mdb-container fluid class="why-container">
    <section class="text-center my-5">
      <h2 class="h1-responsive font-weight-bold my-5">Почему italki?</h2>
      <mdb-row class="container-with-cards">
        <mdb-col md="3" class="why-cards">
          <img src="../assets/1.png" class="img-fluid" alt="Responsive image">
          <h5 class="font-weight-bold my-4">Индивидуальное обучение</h5>
          <hr style="width: 50px; background: black;"/>
          <p
            class="grey-text mb-md-0 mb-5"
          >Выберите своего учителя из более чем 10 000 преподавателей, уроки будут проводиться 1-на-1 с учетом ваших целей и интересов.</p>
        </mdb-col>
        <mdb-col md="3" class="why-cards">
          <img src="../assets/2.png" class="img-fluid" alt="Responsive image">
          <h5 class="font-weight-bold my-4">Платите за 1 урок</h5>
          <hr style="width: 50px; background: black;"/>
          <p
            class="grey-text mb-md-0 mb-5"
          >На italki вы можете платить за 1 урок по цене, которая устроит вас больше всего</p>
        </mdb-col>
        <mdb-col md="3" class="why-cards">
          <img src="../assets/3.png" class="img-fluid" alt="Responsive image">
          <h5 class="font-weight-bold my-4">В любое время, в любом месте</h5>
          <hr style="width: 50px; background: black;"/>
          <p
            class="grey-text mb-md-0 mb-5"
          >Берите онлайн-уроки в то время и в том месте, которые вам подходят.</p>
        </mdb-col>
      </mdb-row>
    </section>
    <section>
        <mdb-row class="image-cont">
            <img src="../assets/5.png" class="img-fluid" alt="Responsive image">
            <img src="../assets/4.png" class="img-fluid" alt="Responsive image">
            <img src="../assets/6.jpg" class="img-fluid" alt="Responsive image">
            <img src="../assets/7.png" class="img-fluid" alt="Responsive image">
            <img src="../assets/8.jpg" class="img-fluid" alt="Responsive image">
            <img src="../assets/9.jpg" class="img-fluid" alt="Responsive image">
        </mdb-row>
    </section>
  </mdb-container>
</template>

<script>
import { mdbContainer, mdbRow, mdbCol } from "mdbvue";
export default {
  name: "FeaturesPage",
  components: {
    mdbContainer,
    mdbRow,
    mdbCol
  }
};
</script>

<style>
.why-container{
    max-width: 1000px;
    display: flexbox;
}
.container-with-cards{
    display:flexbox;
    justify-content: center;
}
.why-cards {
  background: white;
  border-radius: 5px;
  margin: 15px 15px;
}
.why-cards img{
    height: 201px;
}
.image-cont{
    display: flexbox;
    justify-content: center;
}
.image-cont img{
    height: 50px;
    margin: 10px;
}
</style>