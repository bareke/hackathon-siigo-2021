<template>
<div class="container">
  <div class="card">
    <div class="card-body text-center">
        <h1>Bienvenido</h1>
        <div class="row">
          <div class="col-sm-6">
              <ButtonRedirect  @click="redirectJoin" displayTxt="UNIRME" typeBtn="btn-success"/>
          </div>
          <div class="col-sm-6">
              <ButtonRedirect @click="redirectNewGame" displayTxt="CREAR" typeBtn="btn-danger"/>
          </div>
        </div>
    </div>
  </div>
</div>
</template>

<script>
import ButtonRedirect from "@/components/ButtonRedirect";

export default {
  name: "Home",
  components: {
    ButtonRedirect
  },
  methods:{
    redirectNewGame() {
      this.$router.push({
        name: "Game",
        params: {},
      });
    },
    redirectJoin() {
      this.$router.push({
        name: "Join",
        params: {},
      });
    }
  }
};
</script>
