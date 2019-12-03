<template>
  <mdb-container fluid class="why-container">
    <section class="text-center my-5">
      <h2 class="h1-responsive font-weight-bold my-5">Последние отзывы</h2>
      <mdb-row class="container-with-cards">
        <mdb-col md="3" class="why-cards">
          <h5 class="font-weight-bold my-4">ПОТРЯСАЮЩЕЕ СТРЕДСТВО ДЛЯ ПУТЕШЕСТВИЙ</h5>
          <img src="../assets/f1.jpg" class="img-fluid" alt="Responsive image">
          <hr style="width: 50px; background: black;"/>
          <p
            class="grey-text mb-md-0 mb-5"
          >После 5 уроков я нахожусь в приятном шоке от того, сколько оказывается можно выучить за такой короткий промежуток времени. Мой учитель не только общается со мной исключительно на итальянском, а еще отправляет мне письменные задания и небольшие аудио для самостоятельной работы.</p>
        </mdb-col>
        <mdb-col md="3" class="why-cards">
          <h5 class="font-weight-bold my-4">СЕРВИС С УЛЫБКОЙ</h5>
          <img src="../assets/f3.jpg" class="img-fluid" alt="Responsive image">
          <hr style="width: 50px; background: black;"/>
          <p
            class="grey-text mb-md-0 mb-5"
          >Благодаря самостоятельным занятиям и помощи преподавателей italki мой результат за первый в жизни экзамен IELTS составил 7.5 баллов.</p>
        </mdb-col>
        <mdb-col md="3" class="why-cards">
          <h5 class="font-weight-bold my-4">italki очень выручил меня во время учебы за границей</h5>
          <img src="../assets/f2.jpg" class="img-fluid" alt="Responsive image">
          <hr style="width: 50px; background: black;"/>
          <p
            class="grey-text mb-md-0 mb-5"
          >italki идеально подходит тем людям, у которых мало времени, чей бюджет не позволяет оплачивать частного преподавателя, и особенно тем, кому нравится общаться с людьми со всего света.</p>
        </mdb-col>
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
    height: 150px;
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