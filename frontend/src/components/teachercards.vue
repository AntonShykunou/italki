<template>
  <div class="teachercontainer">
    <h1>Более 10 000 преподавателей. <span style="color: red;">Любой язык.</span></h1>
    
  </div>
</template>

<script>
export default {
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
    }
  }
</script>

<style>
.teachercontainer{
    overflow: hidden;
    width: 100%;
    height: 100vh;
    display: block;
    text-align: center;
    min-width: 960px;
    padding-left: 1rem;
    padding-right: 1rem;
    margin-top: 15px;
    border: 1px solid red;
}
</style>