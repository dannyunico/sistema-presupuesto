from rest_framework import serializers

from .models import Material, Herramientas, LaborIndirecta, Factura, Presupuesto




class MaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'codigo', 'title', 'unidad', 'precio','cantidad']

class HerramientasSerializers(serializers.ModelSerializer):

	class Meta:

		model = Herramientas
		fields = ['id', 'codigo', 'titulo', 'COP', 'precio']

class LaborIndirectaSerializers(serializers.ModelSerializer):

	class Meta:

		model = LaborIndirecta
		fields = ['id', 'codigo', 'nombre', 'jornal']

class FacturaSerializers(serializers.ModelSerializer):


	class Meta:

		model = Factura
		fields = ['id', 'Titulo', 'Numero_Factura', 'Cod_Factura', 'Material', 'Herramientas', 'LaborIndirecta']
		depth = 1
	#Herramientas = HerramientasSerializers( many = True)
	#LaborIndirecta = LaborIndirectaSerializers( many = True)

	#def to_representation(self, instance):

		#response = super().to_representation(instance)
		#response['Material'] = MaterialSerializers(instance.Material).data
		#response['Herramientas'] = HerramientasSerializers(instance.Herramientas).data
		#response['LaborIndirecta'] = LaborIndirectaSerializers(instance.LaborIndirecta).data
		#return response



	
class PresupuestoSerializers(serializers.ModelSerializer):

	class Meta:

		model = Presupuesto
		fields = ['Factura']

	def to_representation(self, instance):

		response = super().to_representation(instance)
		response['Factura'] = FacturaSerializers(instance.Factura).data
		return response




	





		



    





