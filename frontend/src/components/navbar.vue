<template>
  <div>
    <div class="navbar">
            <vs-navbar v-model="activeItem" class="nabarx">
              <div slot="title">
                <vs-navbar-title>
                  <b-link to="home">
                    <img src="../assets/logo.png" alt style="max-height:70px; width: 100px;" />
                  </b-link>
                </vs-navbar-title>
              </div>
              <vs-navbar-item index="0">
                <b-button pill variant="outline-light" to="sign in">Войти</b-button>
              </vs-navbar-item>
              <vs-navbar-item index="1">
                <b-button
                  pill
                  variant="outline-light"
                  style="margin: 0 10px;"
                  to="sing up"
                >Зарегестрироваться</b-button>
              </vs-navbar-item>
              <vs-navbar-item index="2">
                <b-button pill variant="outline-light" to="be teacher">Стать преподавателем</b-button>
              </vs-navbar-item>
            </vs-navbar>
    </div>
    <header class="v-header container">
      <div class="fullscreen-video-wrap">
        <video autoplay muted loop>
          <source src="../assets/vheadvideo.mp4" type="video/mp4" />
        </video>
      </div>
        <div class="header-overlay"></div>
        <div class="header-content">
          <h1>Говори свободно на любом языке</h1>
          <h3>Выберите своего учителя из более чем 10 000 преподавателей,<br> уроки будут проводиться 1-на-1 с учетом ваших целей и<br> интересов.</h3>
        </div>
    </header>
  </div>
</template>


<script>
export default {
  data: () => ({
    activeItem: 0
  })
};
</script>

<style >
.v-header{
  overflow: hidden;
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: left;
  color: white;
}
.container{
  min-width: 960px;
  padding-left: 1rem;
  padding-right: 1rem;
  margin: auto;
  text-align: left;
}
.navbar{
  width: 100%;
  position: fixed;
  top: 0;
  z-index: 2;
}
.fullscreen-video-wrap{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  margin: 0;
}
.fullscreen-video-wrap video{
  min-width: 100%;
  min-height: 100%;
}
.header-overlay{
  height: 100vh;
  width: 100vw;
  position: absolute;
  top: 0;
  left: 0;
  background: white;
  z-index: 1;
  opacity: 0.2;
}
.header-content{
  position: relative;
  width: 700px;
  top: 30%;
  height: 100px;
  font-family: Roboto,pingfang SC,Times New Roman,Times,serif,sans-serif,Microsoft YaHei,微软雅黑;;
  z-index: 2;
}
.header-content h1{
  font-size: 29px;
  text-transform: uppercase;
}
.header-content h3{
  font-size: 18px;
}
</style>