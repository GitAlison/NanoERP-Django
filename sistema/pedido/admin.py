from django.contrib import admin
from .models import Nota,TipoNota,ItemNota

class ItemNotaInline(admin.TabularInline):
    model = ItemNota
    extra = 1
    can_delete = True

class AdminNota(admin.ModelAdmin):
    inlines = [ItemNotaInline]
    list_display = ['id','cliente','tipo','status']
    list_filter = ('status','tipo')



admin.site.register(Nota,AdminNota)
admin.site.register(TipoNota)
