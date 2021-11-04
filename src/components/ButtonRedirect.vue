<template>
  <button type="button" :class="['btn', typeBtn]">{{ displayTxt }}</button>
</template>

<script>
export default {
  name: "ButtonRedirect",
  props: {
    displayTxt:String,
    typeBtn:String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
