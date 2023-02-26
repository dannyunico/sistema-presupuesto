<template>
  <div id="app">
    
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
.table-fac-select .vs__selected{
  display: none !important;
}
.table-fac-select .vs__search{
  width: 100px;
}
.table-fac-select .vs__dropdown-option--selected{
  display: none !important;
}


</style>
