<template>
  <div>
    <mdb-navbar dark class="navbar" position="top" style="width:100%;" scrolling>
      <a class="navbar-brand" href="#">
        <img src="../assets/logo.png" width="100" height="60" alt="mdb logo" to="{ name: home}" />
      </a>
      <mdb-navbar-toggler>
        <mdb-navbar-nav right>
          <mdb-btn outline="light" darkWaves rounded @click.native="login = true">Sign in</mdb-btn>
          <mdb-btn outline="light" darkWaves rounded @click.native="register = true">Sign up</mdb-btn>
          <mdb-btn outline="light" darkWaves rounded ><router-link :to="{ name: 'teachers'}">Be a teacher</router-link></mdb-btn>
        </mdb-navbar-nav>
      </mdb-navbar-toggler>
    </mdb-navbar>
    <header class="v-header container">
      <div class="fullscreen-video-wrap">
        <video autoplay muted loop>
          <source src="../assets/vheadvideo.mp4" type="video/mp4" />
        </video>
      </div>
      <div class="header-overlay"></div>
      <div class="header-content">
        <h1>Говори свободно на любом языке</h1>
        <h3>
          Выберите своего учителя из более чем 10 000 преподавателей,
          <br />уроки будут проводиться 1-на-1 с учетом ваших целей и
          <br />интересов.
        </h3>
      </div>
    </header>
    <mdb-container>
      <mdb-modal :show="login" @close="login = false" login>
        <mdb-modal-header class="mx-3 text-center">
          <mdb-modal-title tag="h3" bold class="w-100 my">Sign in</mdb-modal-title>
        </mdb-modal-header>
        <mdb-modal-body class="mx-3">
          <mdb-input label="Your email" type="email" class="mb-3 grey-text" />
          <mdb-input label="Enter password" type="password" class="pb"></mdb-input>
          <p class="font-small blue-text d-flex justify-content-end mb-3">
            <a class="ml-1">Forgot Password?</a>
          </p>
          <div class="text-center mb">
            <mdb-btn color="deep-orange" class="btn" block rounded>Sign In</mdb-btn>
          </div>
        </mdb-modal-body>
        <mdb-modal-footer class="mx-3 pt-3 mb-1" end>
          <p class="font-small grey-text">
            Not a member?
            <a @click.native="register = false" class="blue-text ml-1">Sign Up</a>
          </p>
        </mdb-modal-footer>
      </mdb-modal>
      <mdb-modal :show="register" @close="register = false">
        <mdb-modal-header class="text-center">
          <mdb-modal-title tag="h4" bold class="w-100">Sign up</mdb-modal-title>
        </mdb-modal-header>
        <mdb-modal-body class="mx-3 grey-text">
          <mdb-input label="Your username" icon="user" class="mb-5" />
          <mdb-input label="Your email" icon="envelope" type="email" class="mb-5" />
          <mdb-input label="Your password" icon="lock" type="password" />
        </mdb-modal-body>
        <mdb-modal-footer center>
          <mdb-btn @click.native="register = false" color="deep-orange">Sign Up</mdb-btn>
        </mdb-modal-footer>
      </mdb-modal>
    </mdb-container>
    <teachercards />
    <why/>
    <guide/>
    <feedbacks/>
    <started/>
    <foot/>
  </div>
</template>


<script>
import teachercards from "./teachercards";
import why from "./why_us";
import guide from "./guide";
import feedbacks from "./feedbacks";
import started from "./get_started";
import foot from "./footer";


import {
  mdbContainer,
  mdbBtn,
  mdbModal,
  mdbModalHeader,
  mdbModalBody,
  mdbInput,
  mdbModalFooter,
  mdbModalTitle,
  mdbNavbar,
  mdbNavbarToggler,
  mdbNavbarNav,
} from "mdbvue";

export default {
  name: "ModalExamplesPage",
  components: {
    mdbContainer,
    mdbBtn,
    mdbModal,
    mdbModalHeader,
    mdbModalBody,
    mdbInput,
    mdbModalFooter,
    mdbModalTitle,
    mdbNavbar,
    mdbNavbarToggler,
    mdbNavbarNav,
    //--------------------------------
    teachercards,
    why,
    guide,
    feedbacks,
    started,
    foot
  },
  data() {
    return {
      login: false,
      loading: true,
      register: false
    };
  }
};
</script>

<style >
mdb-container {
  margin: 0;
  padding: 0;
}
.v-header {
  overflow: hidden;
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: left;
  color: white;
}
.container {
  min-width: 960px;
  padding-left: 1rem;
  padding-right: 1rem;
  margin: auto;
  text-align: left;
}
.navbar {
  width: 100%;
  top: 0;
  z-index: 2;
  position: fixed;
  background: rgb(255, 92, 43);
  opacity: 0.8;
}
.fullscreen-video-wrap {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  margin: 0;
}
.fullscreen-video-wrap video {
  min-width: 100%;
  min-height: 100%;
}
.header-overlay {
  height: 100vh;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: white;
  z-index: 1;
  opacity: 0.2;
}
.header-content {
  position: relative;
  width: 700px;
  top: 30%;
  height: 100px;
  font-family: Roboto, pingfang SC, Times New Roman, Times, serif, sans-serif,
    Microsoft YaHei, 微软雅黑;
  z-index: 2;
}
.header-content h1 {
  font-size: 29px;
  text-transform: uppercase;
}
.header-content h3 {
  font-size: 18px;
}
</style>