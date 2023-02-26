<template>
    <div class="container">
        <div class="main-list__items"
                v-for=" (m, $index) in materiales "
                :key="m.id">
                <div class="main-list__item">
                    {{ m.title }}
                </div>
                <div class="main-list__item">
                    {{ m.unidad }}
                </div>
                <div class="main-list__item">
                    {{ m.codigo }}
                </div>
                <div class="main-list__item">
                    {{ m.precio }}
                </div>
                <div class="main-list__item">
                    <router-link :to="`materialesview/${m.id}/edit`">Editar</router-link>
                    <router-link class="list-item__delete" :to="`materialesview/${m.id}/delete`" >Borrar</router-link>
                </div>
            </div>
    </div>
</template>

<script>

import axios from 'axios'

export default{

    name: 'materiales',
    created() {
        this.getMaterial()
    },
    mounted(){
        console.log(this.$route)
    },  
    data(){
        return{
            materialId: this.$route.params.materialId,
            materiales: [],
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
        }
    },
}

</script>

