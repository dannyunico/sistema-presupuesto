<template>
    <div class="container">
        <div class="main-title text-center">
            <h2>¿Quieres eliminar este material?</h2>
        </div>
        <div class="main-content">
            <p>Nombre: {{ this.element.title }} </p>
            <p>Unidad: {{ this.element.unidad }} </p>
            <p>Código: {{ this.element.codigo }} </p>
            <p>Precio: {{ this.element.precio }} </p>
        </div>
        <div class="main-btn" >
            <b-button size="sm" variant="danger" @click="deleteMaterial" >Eliminar</b-button>
            <b-button size="sm" @click="$router.go(-1)" >Cancelar</b-button>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default{

    created() {
        this.getMaterial()
    },
    data(){
        return{
            materialId: this.$route.params.materialId,
            element:{
                title: '',
                unidad: '',
                codigo: '',
                precio: ''
            }
        }
    },
    methods:{
        getMaterial(){
            const path = `http://127.0.0.1:8000/material/${this.materialId}/`;
            axios.get(path)
                .then(r => {
                    this.element.title = r.data.title
                    this.element.unidad = r.data.unidad
                    this.element.precio = r.data.precio
                    this.element.codigo = r.data.codigo
                    
                })
                .catch(error => console.log(error))
        },
        deleteMaterial(){
            const path = `http://127.0.0.1:8000/material/${this.materialId}/`;
            axios.delete(path).then((r) => {
                    location.href="/materialesView"
                })
                .catch(error => console.log(error))
        }
    }
}

</script>