<template>
  <div class="GOL">
    <NavBar/>
    <section class="hero is-fullheight">
      <div class="main-content-app">
        <div class="container is-paddingless">
          <div class="columns box is-fullwidth is-gapless">
            <div class="column is-12">
              <transition mode="out-in" name="fade">
                <keep-alive>
                  <Grid
                    v-if="mainComponent == 'gamePage'"
                    :message="message"
                    :current-speed="speed"
                  />
                </keep-alive>
              </transition>
            </div>
          </div>
        </div>
      </div>
      <footer class="footer">
        <div class="container">
          <div class="columns">
            <div class="column is-half is-offset-one-quarter">
              <Controls
                :is-running="isRunning"
                :main-component="mainComponent"
                @send="delegate($event)"
              />
            </div>
          </div>
        </div>
      </footer>
    </section>
  </div>
</template>

<script>
import Vue from "vue";
import Controls from "@/components/ControlsPanel.vue";
import Grid from "@/components/GridBoard.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "App",
  components: {
    Grid,
    Controls,
    NavBar,
  },
  data() {
    return {
      message: "",
      isRunning: false,
      speed: 125,
      intervalID: 0,
      mainComponent: "gamePage",
      selectedScenario: "scenario",
    };
  },
  created() {},
  methods: {
    delegate: function (event) {
      if (event === "play") {
        this.isRunning = !this.isRunning;
        this.restartInterval();
      } else {
        this.updateMessage(event);
      }
    },
    updateMessage: function (newMessage) {
      this.message = newMessage;
      Vue.nextTick(this.resetMessage);
    },
    resetMessage: function () {
      this.message = "";
    },
    restartInterval: function () {
      clearInterval(this.intervalID);
      if (this.isRunning) {
        this.intervalID = setInterval(
          this.updateMessage,
          50000 / this.speed,
          "nextStep"
        );
      }
    },
  },
};
</script>

<style>
html,
body {
  background-image: linear-gradient(
    to right top,
    #41434d,
    #373943,
    #35363e,
    #282a36
  );
  color: #000;
  font-family: "Dosis", Helvetica, sans-serif;
  margin: 0px;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  color: #fff;
}

.main-content-app {
  align-items: stretch !important;
  padding-top: 80px;
  padding-bottom: 12px;
}

.footer {
  background-color: #282a36 !important;
}

.hr {
  position: relative;
  border-top: 2px solid #414b5c;
  margin: 0px;
  bottom: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.35s linear;
}

.fade-enter,
.fade-leave-active {
  opacity: 0;
}
</style>