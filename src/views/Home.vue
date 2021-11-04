<template>
  <div class="home">
    <Game />
    <Join />
  </div>
</template>

<script>
// @ is an alias to /src
import Game from "@/views/Game.vue";
import Join from "@/views/Join.vue";

export default {
  name: "Home",
  components: {
    Game,
    Join,
  },
};
</script>
