<template>
    <div class="container">
        <div class="main-title">
            <h2>Materiales</h2>
            <router-link class="addNew" :to="{ name: 'createMaterial' }" >Añadir nuevo material</router-link>
        </div>
        <div class="main-list">
            <div class="main-list__header">
                <div class="list-header__item">
                    <span>Nombre</span>
                </div>
                <div class="list-header__item">
                    <span>Unidad</span>
                </div>
                <div class="list-header__item">
                    <span>Código</span>
                </div>
                <div class="list-header__item">
                    <span>Precio</span>
                </div>
                <div class="list-header__item">
                    <span></span>
                </div>
            </div>
            <Materiales />
        </div>
    </div>
</template>

<script>


import Materiales from '@/components/Materiales/materialTest.vue'

export default{
    
    data(){
        return{
            
        }
    },
    
    components:{
        Materiales
    }
}

</script>

<style lang="css" scoped>

.main-list__items, .main-list__header{
    display: flex;
    justify-content: space-between;
    text-align: start;
}
.main-list__item, .list-header__item{
    width: 20%;
}
.main-title{
    display: flex;
    justify-content: space-between;
    align-items: center;
}

</style>