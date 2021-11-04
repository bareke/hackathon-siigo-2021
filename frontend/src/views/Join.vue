<template>
  <div class="container">
    <h2 class="mt-4">Ingresa el codigo</h2>
    <div style="text-align: center;padding-left: 30%;padding-right: 30%;">
      <input  class="form-control mt-4" style="width: 100%; padding-left: 10px;" type="text"  v-model="nameUser"  placeholder="Ingresa nombre de usuario" required>
      <input class="form-control mt-4" style="width: 100%; padding-left: 10px;" type="text"  v-model="codeJoin"  placeholder="Ingresa el código de conexion" required>
    </div>

    <br>
    <!--<button class="btn btn-success mt-3" @click="actionAddUser({id:'3242',hex:this.codeJoin,active:0})">Ingresar</button>-->
    <button class="btn btn-success mt-3" @click="JoinGame({id:'3242',hex:this.codeJoin,active:1,name:this.nameUser})">Ingresar</button>
  </div>

</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: "Join",
  methods:{
    redirectGame(username,idUser) {
      //this.$toast.success(`Partida creada`,{position:"top-right"});
      this.$router.push({
        name: "Game",
        params: {nameUser:username,idUser:idUser},
      });
    },
    JoinGame(user){
      this.$toast.success(`Te haz unido a una partida`,{position:"top-right"});
      user.id = this.generateRandomToJoin();
      this.actionAddUser(user);
      this.redirectGame(user.name,user.id);
    },
     generateRandomToJoin() {
      const genRanHex = (size) =>
        [...Array(size)]
          .map(() => Math.floor(Math.random() * 16).toString(16))
          .join("");

      //this.generateJoin = genRanHex(12);
      return genRanHex(6);
    },

    ...mapActions(['actionAddUser']),
  }
}
</script>

<style>

</style>
