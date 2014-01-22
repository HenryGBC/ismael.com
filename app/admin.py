from django.contrib import admin
from models import Tipo, Plato, Ingrediente, Menu
# Register your models here.

class PlatoAdmin(admin.ModelAdmin):
	filter_vertical = ('ingredientes',)


admin.site.register(Tipo)
admin.site.register(Plato, PlatoAdmin)
admin.site.register(Ingrediente)
admin.site.register(Menu)