from django.contrib import admin

from .models import Material, Herramientas, LaborIndirecta, Factura, Presupuesto

# Register your models here.

admin.site.register(Material)
admin.site.register(Herramientas)
admin.site.register(LaborIndirecta)
admin.site.register(Factura)
admin.site.register(Presupuesto)

