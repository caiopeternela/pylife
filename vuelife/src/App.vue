<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DynaPuff&display=swap');

* {
  font-family: 'DynaPuff', cursive;
}

#app {
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>