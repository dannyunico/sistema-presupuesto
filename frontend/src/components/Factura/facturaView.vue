<template lang="html">
    <div class="container">
        <h2>Factura</h2>
        <div>
          <div class="table-fac">
            <div v-for="(m ) in materiales">
              {{ m.id }}
            </div>
          </div>
        </div>
        <pre> {{ $data.facturas }} </pre>
    </div>
</template>

<script>

import axios from 'axios'

export default{
    name: 'Factura',
    created() {
        this.getMaterial();
        this.getFactura();
        this.replaceMaterials()
    },
    data(){
      return{
          materiales: [],
          facturas: [],
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
    getFactura(){
      const path = `http://127.0.0.1:8000/factura/`;
      axios.get(path)
          .then(r => {
              this.facturas = r.data
              
          })
          .catch(error => console.log(error))
    },
    
  },
  computed:{

  },
  watch:{
    
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