from .models import Material, Herramientas, LaborIndirecta, Factura, Presupuesto
from rest_framework import viewsets
from .serializers import MaterialSerializers, HerramientasSerializers, LaborIndirectaSerializers, FacturaSerializers, PresupuestoSerializers
from rest_framework.response import Response

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
	serializer_class = FacturaSerializers

	def get_queryset(self):
		factura = Factura.objects.all()
		return factura
	
	def create(self, request, *args, **kwargs):
		data = request.data

		new_factura = Factura.objects.create(
			Titulo=data["Titulo"], Numero_Factura=data["Numero_Factura"], Cod_Factura=data["Cod_Factura"])
		
		new_factura.save()

		for material in data["Material"]:
			material_obj = Material.objects.get(id=material["id"])
			new_factura.Material.add(material_obj)

		for herramienta in data["Herramientas"]:
			herramienta_obj = Herramientas.objects.get(id=herramienta["id"])
			new_factura.Herramientas.add(herramienta_obj)

		for laborInderecta in data["LaborIndirecta"]:
			laborInderecta_obj = LaborIndirecta.objects.get(id=laborInderecta["id"])
			new_factura.LaborIndirecta.add(laborInderecta_obj)
		
		serializer = FacturaSerializers(new_factura)

		return Response(serializer.data)

class ViewsPresupuestoSerializers(viewsets.ModelViewSet):

	queryset = Presupuesto.objects.all()

	serializer_class = PresupuestoSerializers





    

	

		 