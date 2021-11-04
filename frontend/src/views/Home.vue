<template>
<div class="container">
  <div class="card">
    <div class="card-body text-center card-home">
        <h1>Encuentra el bug en el sistema</h1>
        <div class="row" style="padding-left: 30%; padding-right: 31%; margin-top: 7%;">
          <div class="col-sm-6">
              <ButtonRedirect class="btn1" @click="redirectJoin" displayTxt="UNIRME" typeBtn="btn-success"/>
          </div>
          <div class="col-sm-6">
              <ButtonRedirect  class="btn2" @click="redirectNewGame" displayTxt="CREAR" typeBtn="btn-danger"/>
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
      this.$toast.success(`Partida creada`,{position:"top-right"});
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

<style scoped>
.card-home{
  padding-top: 10%;
  padding-bottom: 10%;
  padding-left: 17%;
  padding-right: 17%;
}

.btn1 .btn2{
  padding: 80px;
}
</style>
