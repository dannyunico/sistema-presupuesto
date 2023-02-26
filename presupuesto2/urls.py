
from rest_framework import routers
from .api import ViewsMaterial, ViewsHerramientas, ViewsIndirectaSerializers, ViewsFacturaSerializers, ViewsPresupuestoSerializers


router = routers.DefaultRouter()

router.register('material', ViewsMaterial, 'material')
router.register('herramientas', ViewsHerramientas, 'herramientas')
router.register('laborindirecta', ViewsIndirectaSerializers, 'laborindirecta')
router.register('factura', ViewsFacturaSerializers, 'factura')
router.register('presupuesto', ViewsPresupuestoSerializers, 'presupuesto')

urlpatterns = router.urls