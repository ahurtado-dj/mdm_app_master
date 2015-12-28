from django.contrib import admin

# Register your models here.
from .models import Tercero

class TerceroAdmin (admin.ModelAdmin):
	list_display = ('ter_ident','ter_tipodoc','ter_nom','ter_ap1')
	

admin.site.register(Tercero,TerceroAdmin)
