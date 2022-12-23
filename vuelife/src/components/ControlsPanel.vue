<template>
  <div class="box">
    <div class="field has-addons has-addons-centered is-marginless">
      <p class="control">
        <button
          :disabled="mainComponent !== 'gamePage'"
          :class="isRunning ? 'green' : 'red'"
          class="button play"
          title="play"
          @click="send('play')"
        >
          <v-icon v-show="!isRunning">mdi-play</v-icon>
          <v-icon v-show="isRunning">mdi-pause</v-icon>
        </button>
      </p>
      <p class="control">
        <button
          :disabled="mainComponent !== 'gamePage'"
          class="button reset"
          title="clear grid"
          @click="send('redoSession')"
        >
          <v-icon> mdi-restart</v-icon>
        </button>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isRunning: {
      default: false,
      type: Boolean,
    },
    mainComponent: {
      default: "gamePage",
      type: String,
    },
  },
  methods: {
    send: function (event) {
      this.$emit("send", event);
    },
  },
};
</script>

<style scoped>

.box {
  padding: 0;
  background-color: #282a36;
}

.green {
  background-color: #50fa7b;
}

.red {
  background-color: #ff5555;
}

.reset {
  background-color: #f1fa8c
}

.button {
  border-style: hidden;
}
</style>