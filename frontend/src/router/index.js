import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListMaterials from '@/components/Materiales/ListMaterials'
import editMaterial from '@/components/Materiales/editMaterial'
import deleteMaterial from '@/components/Materiales/deleteMaterial'
import createMaterial from '@/components/Materiales/createMaterial'

import facturaView from '@/components/Factura/facturaView'


import materialesView from '@/views/materialesView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/Materiales',
      name: 'ListMaterials',
      component: ListMaterials
    },
    {
      path: '/Materiales/new',
      name: 'createMaterial',
      component: createMaterial
    },
    {
      path: '/materialesView',
      name: 'materialesView',
      component: materialesView
    },
    {
      path: '/materialesview/:materialId/edit',
      name: 'editMaterial',
      component: editMaterial
    },
    {
      path: '/materialesview/:materialId/delete',
      name: 'deleteMaterial',
      component: deleteMaterial
    },
    {
      path: '/factura',
      name: 'facturaView',
      component: facturaView
    },
    
    
  ],
  mode: 'history'
})
