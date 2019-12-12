<template>
  <mdb-container>
    <h2 class="h1-responsive font-weight-bold text-center my-5">Как это работает?</h2>
    <mdb-row>
      <mdb-col lg="5">
        <mdb-view class="rounded z-depth-2 mb-lg-0 mb-4" hover>
          <video autoplay muted loop>
            <source src="../assets/howit1.mp4" type="video/mp4" />
          </video>
          <a>
            <mdb-mask overlay="white-slight" waves />
          </a>
        </mdb-view>
      </mdb-col>
      <mdb-col lg="7">
        <h3 class="font-weight-bold mb-3 p-0">
          <strong>&#9312; Выберите преподавателя</strong>
        </h3>
        <p>Посмотрите видеопрезентацию преподавателя и почитайте отзывы других учеников.</p>
      </mdb-col>
    </mdb-row>
    <hr class="my-5" />
    <mdb-row>
      <mdb-col lg="7">
        <h3 class="font-weight-bold mb-3 p-0">
          <strong>&#9313; НАЗНАЧЬТЕ УРОК</strong>
        </h3>
        <p>Планируйте уроки так, чтобы их дата и время подходили вам.</p>
      </mdb-col>
      <mdb-col lg="5">
        <mdb-view class="rounded z-depth-2 mb-lg-0 mb-4" hover>
          <video autoplay muted loop>
            <source src="../assets/howit1.mp4" type="video/mp4" />
          </video>
        </mdb-view>
      </mdb-col>
    </mdb-row>
    <hr class="my-5" />
    <mdb-row>
      <mdb-col lg="5">
        <mdb-view class="rounded z-depth-2 mb-lg-0 mb-4" hover>
          <video autoplay muted loop>
            <source src="../assets/howit1.mp4" type="video/mp4" />
          </video>
        </mdb-view>
      </mdb-col>
      <mdb-col lg="7">
        <h3 class="font-weight-bold mb-3 p-0">
          <strong>&#9313; НАЧНИТЕ СВОЁ ПУТЕШЕСТВИЕ</strong>
        </h3>
        <p>
          Используй любые программы для видеозвонков, чтобы связаться с преподавателем и начать заниматься!
        </p>
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCol,
  mdbMask,
  mdbView
} from "mdbvue";
export default {
  name: "BlogPage",
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbMask,
    mdbView
  }
};
</script>

<style>
</style>