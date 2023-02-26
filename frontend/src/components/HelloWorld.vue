<template>
  <div class="container">
      <h2>Factura</h2>
      <div>
        <div class="factura-name">
          <span>Nombre</span>
          <input type="text" v-model="form.Titulo">
        </div>
        <div class="factura-number">
          <span>Numero de factura</span>
          <input type="text" v-model="form.Numero_Factura">
        </div>
        <div class="factura-code">
          <span>Código de factura</span>
          <input type="text" v-model="form.Cod_Factura">
        </div>
        <div class="d-flex table-fac">
              <v-select 
                :options="buscarMaterial" 
                v-model="form.Material" 
                label="title" 
                multiple
                placeholder="Nombre"
                class="table-fac-select">
              </v-select>
              <v-select 
                :options="buscarHerramientas" 
                v-model="form.Herramientas" 
                label="titulo" 
                multiple
                placeholder="h"
                class="table-fac-select">
              </v-select>
              <v-select 
                :options="buscarLabor" 
                v-model="form.LaborIndirecta" 
                label="nombre" 
                multiple
                placeholder="l"
                class="table-fac-select">
              </v-select>
              
            <div class="materiales">
              <div v-for=" (m, $index ) in form.Material">
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
       
        <b-button @click="sendFactura" variant="primary">Enviar</b-button>
      </div>
  </div>
</template>

<script>

import axios from 'axios'

export default{
  created() {
      this.getMaterial();
      this.getHerramienta();
      this.getLaborIndirecta();
  },
  data(){
    return{
        materiales: [],
        materialesSeleccionado: [],
        herramientas: [],
        laborIndirecta: [],
        facturas: [],
        totalSuma: 0,
        buscador: '',
        form:{
          Titulo: '',
          Numero_Factura: '',
          Cod_Factura: '',
          Material: [],
          Herramientas: [],
          LaborIndirecta: [],
        },
        forms: [],
    }
},
methods:{
  getMaterial(){
    const path = `http://127.0.0.1:8000/material/`;
    axios.get(path)
        .then(r => {
            this.materiales = r.data
            
        })
        .catch(error => console.log(error))
  },
  getHerramienta(){
    const path = `http://127.0.0.1:8000/herramientas/`;
    axios.get(path)
        .then(r => {
            this.herramientas = r.data
            
        })
        .catch(error => console.log(error))
  },
  getLaborIndirecta(){
    const path = `http://127.0.0.1:8000/laborindirecta/`;
    axios.get(path)
        .then(r => {
            this.laborIndirecta = r.data
            
        })
        .catch(error => console.log(error))
  },
  sendFactura(){
    const path = `http://127.0.0.1:8000/factura/`;
    axios.post(path, this.form)
        .then(r => {
          this.form.Titulo = r.data.Titulo
          this.form.Numero_Factura = r.data.Numero_Factura
          this.form.Cod_Factura = r.data.Cod_Factura
          this.form.Material = r.data.Material
          this.form.Herramientas = r.data.Herramientas
          this.form.LaborIndirecta = r.data.LaborIndirecta
          alert('Creado')
        })
        .catch(error => console.log(error))
  },
  addMaterial(id){
    var indice = this.materiales.findIndex( elemento => {
      return elemento.codigo === id;
    });
    if (indice > -1 ){
      var element = this.materiales.splice(indice, 1)[0]
      this.form.Material.unshift(element.id)
    }
    
  },
  deleteMaterial(id){
    this.form.Material.splice(id, 1)
    
    this.sumaTotal()
  },
  
  increment (indice) {
    this.form.Material[indice].cantidad++;
    this.sumaTotal()
  
  },
  decrement (indice) {
    if( this.form.Material[indice].cantidad == 1 ){
      alert('No más')
    }
    else{
      this.form.Material[indice].cantidad--;
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
  buscarHerramientas(){
    return this.herramientas.filter( herramienta => {
      return herramienta.titulo.includes(this.buscador);
    } );
  },
  buscarLabor(){
    return this.laborIndirecta.filter( labor => {
      return labor.codigo.includes(this.buscador);
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