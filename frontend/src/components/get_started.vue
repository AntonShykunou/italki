<template>
  <div class="cont">
    <div class="white"></div>
      <mdb-container>
        <mdb-row>
          <mdb-col>
            <div class="learn-more">
              <h1>Изучайте больше, чем просто язык</h1>
              <p>На italki вы приобретете новые языковые навыки, перед вами откроются новые перспективы, здесь вы будете общаться с интереснейшими людьми со всего мира.</p>
              <mdb-btn color="danger">Начни прямо сейчас</mdb-btn>
            </div>
          </mdb-col>
        </mdb-row>
      </mdb-container>
  </div>
</template>

<script>
import { mdbContainer, mdbRow, mdbCol, mdbBtn } from "mdbvue";
export default {
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbBtn
  }
};
</script>

<style>
.learn-more {
  color: white;
  margin: 100px 0px;
  max-width: 400px;
  z-index: 4;
}
.cont {
  position: relative;
  z-index: 100;
  background-image: url(../assets/girls.jpg);
}
.white {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, rgb(243, 119, 36), rgb(255, 255, 255));
  opacity: 0.4;
}
</style>