<template>
  <mdb-container>
    <mdb-btn rounded color="" @click.native="login = true">Sign in </mdb-btn>
    <mdb-modal :show="login" @close="login = false" login>
      <mdb-modal-header class="mx-3 text-center">
        <mdb-modal-title tag="h3" bold class="w-100 my"
          >Sign in</mdb-modal-title
        >
      <Loader v-if="loading"/>
      </mdb-modal-header>
      <mdb-modal-body class="mx-3">
        <mdb-input label="Your email" type="email" class="mb-3 grey-text" />
        <mdb-input
          label="Enter password"
          type="password"
          class="pb"
        ></mdb-input>
        <p class="font-small blue-text d-flex justify-content-end mb-3">
          <a class="ml-1"> Forgot Password?</a>
        </p>
        <div class="text-center mb">
          <mdb-btn color="success-color" class="btn btn-danger" block rounded
            >Sign In</mdb-btn
          >
        </div>
      </mdb-modal-body>
      <mdb-modal-footer class="mx-3 pt-3 mb-1" end>
        <p class="font-small grey-text">
          Not a member? <a class="blue-text ml-1">Sign Up</a>
        </p>
      </mdb-modal-footer>
    </mdb-modal>
  </mdb-container>
</template>

<script>
import Loader from '@/components/Loader'
import {
  mdbContainer,
  mdbBtn,
  mdbModal,
  mdbModalHeader,
  mdbModalBody,
  mdbInput,
  mdbModalFooter,
  mdbModalTitle,
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
    Loader
  },
  data() {
    return {
      login: false,
      loading: true
    };
  }
};
</script>
