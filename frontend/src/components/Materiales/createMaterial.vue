<template>
    <div class="container">
        <div class="main-title">
            <h2> Crear material</h2>
            <a @click="$router.go(-1)" href="#" >Regresar</a>
            
        </div>
        <div class="card-edit">
            <form @submit="onSubmit">
                <div class="form-group">
                    <label for="name"> Nombre</label>
                    <div>
                        <input type="text" name="name" placeholder="Nombre" v-model.trim="form.title">
                    </div>
                </div>
                <div class="form-group">
                    <label for="unidad"> Unidad</label>
                    <div>
                        <input type="text" name="unidad" placeholder="Unidad" v-model.trim="form.unidad">
                    </div>
                </div>
                <div class="form-group">
                    <label for="codigo"> Código</label>
                    <div>
                        <input type="text" name="codigo" placeholder="Código" v-model.trim="form.codigo">
                    </div>
                </div>
                <div class="form-group">
                    <label for="precio"> Precio</label>
                    <div>
                        <input type="text" name="precio" placeholder="Precio" v-model.trim="form.precio">
                    </div>
                </div>
                <div class="form-btn">
                    <b-button type="submit" variant="primary" >Crear</b-button>
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
       
    },
    data(){
        return{
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
            const path = 'http://127.0.0.1:8000/material/';
            axios.post(path, this.form)
                .then(r => {
                    this.form.title = r.data.title
                    this.form.unidad = r.data.unidad
                    this.form.precio = r.data.precio
                    this.form.codigo = r.data.codigo
                    location.href="/materialesView"
                    alert('Creado')
                })
                .catch(error => console.log(error))
        },
        
        
    }
}

</script>

<style>
</style>