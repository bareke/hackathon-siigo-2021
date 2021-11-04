<template>
  <div class="container">
    <h2 class="mt-4">Ingresa el codigo</h2>
    <input type="text"  v-model="codeJoin"  placeholder="Ingresa el código de conexion">
    <br>
    <button class="btn btn-success mt-3" @click="JoinGame">Ingresar</button>
  </div>
</template>

<script>
export default {
  name: "Join",
  methods:{
    JoinGame(){
      this.store.commit('addUser', {id:123,hex:'jghg233',active:0})
      alert(this.codeJoin);
    },
  }
}
</script>

<style>

</style>
