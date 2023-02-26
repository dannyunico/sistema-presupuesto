<template>
    <div class="container">
        <div class="main-title">
            <h2> Editar material</h2>
            <a @click="$router.go(-1)" href="#" >Regresar</a>
            
        </div>
        <div class="card-edit">
            <form @submit="onSubmit">
                <div class="form-group">
                    <label for="name"> Nombre</label>
                    <div>
                        <input type="text" name="name" v-model.trim="form.title">
                    </div>
                </div>
                <div class="form-group">
                    <label for="unidad"> Unidad</label>
                    <div>
                        <input type="text" name="unidad" v-model.trim="form.unidad">
                    </div>
                </div>
                <div class="form-group">
                    <label for="codigo"> Código</label>
                    <div>
                        <input type="text" name="codigo" v-model.trim="form.codigo">
                    </div>
                </div>
                <div class="form-group">
                    <label for="precio"> Precio</label>
                    <div>
                        <input type="text" name="precio" v-model.trim="form.precio">
                    </div>
                </div>
                <div class="form-btn">
                    <b-button type="submit" variant="primary" >Editar</b-button>
                    <b-button type="submit" variant="warning" :to="{ name: 'materialesView' }" >Cancelar</b-button>
                </div>
            </form>
        </div>
    </div>
</template>


<script>

import axios from 'axios'

export default{
    created() {
        this.getMaterial()
    },
    mounted(){
        console.log(this.$route)
    }, 
    data(){
        return{
            materialId: this.$route.params.materialId,
            form: {
                title: '',
                unidad: '',
                precio: '',
                codigo: '',
            }, 
        }
    },
    methods:{
        onSubmit(evt){
            evt.preventDefault();
            const path = `http://127.0.0.1:8000/material/${this.materialId}/`;
            axios.put(path, this.form)
                .then(r => {
                    this.form.title = r.data.title
                    this.form.unidad = r.data.unidad
                    this.form.precio = r.data.precio
                    this.form.codigo = r.data.codigo
                    location.href="/materialesView"
                    alert('Actualizado')
                })
                .catch(error => console.log(error))
        },
        getMaterial(){
            const path = `http://127.0.0.1:8000/material/${this.materialId}/`;
            axios.get(path)
                .then(r => {
                    this.form.title = r.data.title
                    this.form.unidad = r.data.unidad
                    this.form.precio = r.data.precio
                    this.form.codigo = r.data.codigo
                    
                })
                .catch(error => console.log(error))
        }
        
    }
}

</script>

<style>
</style>