from .models import Material, Herramientas, LaborIndirecta, Factura, Presupuesto
from rest_framework import viewsets
from .serializers import MaterialSerializers, HerramientasSerializers, LaborIndirectaSerializers, FacturaSerializers, PresupuestoSerializers

class ViewsMaterial(viewsets.ModelViewSet):

	queryset = Material.objects.all()

	serializer_class = MaterialSerializers

class ViewsHerramientas(viewsets.ModelViewSet):

	queryset = Herramientas.objects.all()

	serializer_class = HerramientasSerializers

class ViewsIndirectaSerializers(viewsets.ModelViewSet):

	queryset = LaborIndirecta.objects.all()

	serializer_class = LaborIndirectaSerializers

class ViewsFacturaSerializers(viewsets.ModelViewSet):

	queryset = Factura.objects.all()

	serializer_class = FacturaSerializers

class ViewsPresupuestoSerializers(viewsets.ModelViewSet):

	queryset = Presupuesto.objects.all()

	serializer_class = PresupuestoSerializers





    

	

		 