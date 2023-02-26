<template lang="html">
    <div class="container">
        <h2>Materiales</h2>
        <div>
            <div class="d-flex table-fac">
              <v-select 
                :options="buscarMaterial" 
                v-model="materialesSeleccionados" 
                label="title" 
                multiple
                placeholder="Nombre"
                class="table-fac-select">
              </v-select>
              <v-select 
                :options="buscarMaterialCode" 
                v-model="materialesSeleccionados" 
                label="codigo" 
                multiple
                placeholder="Código"
                class="table-fac-select">
              </v-select>
            <div class="materiales">
              <div v-for=" (m, $index ) in materialesSeleccionados">
                <div>
                  {{ m.title }}
                {{ m.precio }}
                  <div class="quantity-toggle">
                    <div class="quantity-toggle">
                      <button @click="decrement($index)">-</button>
                      <span>{{ m.cantidad }}</span>
                      <button @click="increment($index)">+</button>
                    </div>
                  </div>
                  <b-button @click="deleteMaterial($index)" size="sm" variant="danger">Eliminar</b-button>
                </div>
              </div>
            </div>
            <div class="total-material">
              <div v-for="total in totalMaterial" >
                <div>
                  {{ total }}
              </div>
              </div>
            </div>
            <p class="total-total">{{ totalSuma }}</p>
          </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default{
  mounted() {
    axios.get(this.url)
        .then(r => this.materiales = r.data)
        .catch(error => console.log(error));
        this.sumaTotal()
  },
  created(){
    this.sumaTotal()
  },
  data(){
      return{
          materiales: [],
          materialesSeleccionados: [],
          url: 'http://127.0.0.1:8000/material/',
          buscador: '',
          totalSuma: 0
      }
  },
  methods:{
    
    deleteMaterial(id){
      this.materialesSeleccionados.splice(id, 1)
      
      this.sumaTotal()
    },
    
    increment (indice) {
      this.materialesSeleccionados[indice].cantidad++;
      this.sumaTotal()
    
    },
    decrement (indice) {
      if( this.materialesSeleccionados[indice].cantidad == 1 ){
        alert('No más')
      }
      else{
        this.materialesSeleccionados[indice].cantidad--;
      }
      this.sumaTotal()
    },
    sumaTotal(){
      const total = this.buscarMaterialCode && this.totalMaterial.reduce((a,b) => a + b, 0);
      this.totalSuma = total;
    },
  },
  computed:{
    buscarMaterial(){
      return this.materiales.filter( material => {
        return material.title.includes(this.buscador);
      } );
    },
    buscarMaterialCode(){
      return this.materiales.filter( material => {
        return material.codigo.includes(this.buscador);
      } );
    },
    totalMaterial(){
      return this.materialesSeleccionados.map( material => {
        return material = material.precio * material.cantidad
      } );
    },
    
  },
  watch:{
    materialesSeleccionados(){
      const total = this.totalMaterial.reduce((a,b) => a + b, 0);
      this.totalSuma = total;
    }
  }
}

</script>

<style lang="css" scoped >

.materiales, .total-material{
  width: 50%;
  padding: 10px;
}
.total-total{
  text-align: end;
}


</style> 