<template>
  <div>
    <mdb-navbar position="top" dark color="indigo" expand="large" style="z-index: 9998;opacity:1;">
      <mdb-navbar-brand style="color: white;">
        <router-link :to="{ name: 'home'}">Navbar</router-link>
      </mdb-navbar-brand>
      <mdb-navbar-toggler>
        <mdb-navbar-nav right>
          <mdb-nav-item href="#" active @click.native="login = true">Sign in</mdb-nav-item>
          <mdb-nav-item href="#" @click.native="register = true">Sign up</mdb-nav-item>
          <mdb-dropdown tag="li" class="nav-item">
            <mdb-dropdown-toggle tag="a" navLink color="indigo" slot="toggle" waves-fixed>Languages</mdb-dropdown-toggle>
            <mdb-dropdown-menu>
              <mdb-dropdown-item>English</mdb-dropdown-item>
              <mdb-dropdown-item>French</mdb-dropdown-item>
              <mdb-dropdown-item>Russian</mdb-dropdown-item>
            </mdb-dropdown-menu>
          </mdb-dropdown>
        </mdb-navbar-nav>
      </mdb-navbar-toggler>
    </mdb-navbar>
    <div class="check-div">
      <mdb-navbar-nav nav center>
        <mdb-nav-item @click.native="country = true">From</mdb-nav-item>
        <mdb-nav-item @click.native="lang = true">Speak</mdb-nav-item>
        <mdb-nav-item @click.native="price = true">Price</mdb-nav-item>
        <mdb-nav-item>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="defaultUnchecked" />
            <label class="custom-control-label" for="defaultUnchecked">Native speaker</label>
          </div>
        </mdb-nav-item>
      </mdb-navbar-nav>
    </div>
    <!--<div class="container" v-for="card in teachercard"></div>-->
    <teachercard />
    <mdb-container class="cls-with-modal">
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
      <mdb-modal :show="country" @close="country = false">
        <mdb-modal-header class="mx-3 text-center">
          <mdb-modal-title tag="h3" bold class="w-100 my">Countries</mdb-modal-title>
        </mdb-modal-header>
        <mdb-modal-body class="mx-3">
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="eng" />
            <label class="custom-control-label" for="eng">USA</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="french" />
            <label class="custom-control-label" for="french">France</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="rus" />
            <label class="custom-control-label" for="rus">Russia</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="bel" />
            <label class="custom-control-label" for="bel">Belarus</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="uk" />
            <label class="custom-control-label" for="uk">Ukraine</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="can" />
            <label class="custom-control-label" for="can">Canada</label>
          </div>
          <div class="text-center mb">
            <mdb-btn color="deep-orange" class="btn" block rounded>Confirm</mdb-btn>
          </div>
        </mdb-modal-body>
      </mdb-modal>
      <mdb-modal :show="lang" @close="lang = false">
        <mdb-modal-header class="mx-3 text-center">
          <mdb-modal-title tag="h3" bold class="w-100 my">Languages</mdb-modal-title>
        </mdb-modal-header>
        <mdb-modal-body class="mx-3">
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="eng" />
            <label class="custom-control-label" for="eng">English</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="french" />
            <label class="custom-control-label" for="french">French</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="rus" />
            <label class="custom-control-label" for="rus">Russian</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="bel" />
            <label class="custom-control-label" for="bel">Belorusian</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="uk" />
            <label class="custom-control-label" for="uk">Ukrainian</label>
          </div>
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="can" />
            <label class="custom-control-label" for="can">Canada</label>
          </div>
          <div class="text-center mb">
            <mdb-btn color="deep-orange" class="btn" block rounded>Confirm</mdb-btn>
          </div>
        </mdb-modal-body>
      </mdb-modal>
      <mdb-modal :show="price" @close="price = false">
        <mdb-modal-header class="mx-3 text-center">
          <mdb-modal-title tag="h3" bold class="w-100 my">Price</mdb-modal-title>
        </mdb-modal-header>
        <mdb-modal-body class="mx-3">
          <mdb-range-input :min="0" :max="100" :value="50"></mdb-range-input>
        </mdb-modal-body>
      </mdb-modal>
    </mdb-container>
  </div>
</template>

<script>
import {
  mdbRangeInput,
  mdbDropdown,
  mdbDropdownToggle,
  mdbDropdownMenu,
  mdbDropdownItem,
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
  mdbNavItem
} from "mdbvue";
import teachercard from "./teachercard";
export default {
  name: "HelloWorld",
  components: {
    mdbRangeInput,
    mdbDropdown,
    mdbDropdownToggle,
    mdbDropdownMenu,
    mdbDropdownItem,
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
    mdbNavItem,
    //-------------------
    teachercard
  },
  data() {
    return {
      login: false,
      loading: true,
      register: false,
      country: false,
      lang: false,
      price: false
    };
  }
};
</script>

<style>
.cls-with-modal {
  z-index: 9999;
  position: fixed;
  top: 20%;
  left: 25%;
}
.check-div {
  position: fixed;
  margin-top: 55px;
  height: 60px;
  width: 100%;
  padding: 10px;
  background: rgb(31, 209, 253);
  z-index: 9997;
}
#f {
  z-index: 9996;
}
</style>