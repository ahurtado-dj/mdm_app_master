from django.contrib import admin

# Register your models here.
from .models import Persona

class PersonaAdmin (admin.ModelAdmin):
	list_display = ('identificacion','tipo_identificacion','nombres','apellidos')
	

admin.site.register(Persona,PersonaAdmin)
