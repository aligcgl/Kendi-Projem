from django.contrib import admin

from .models import MüşteriModel


class MüşteriAdmin(admin.ModelAdmin):
    search_fields=("isim","soyisim")
    list_display=("isim", "soyisim","eposta")

admin.site.register(MüşteriModel,MüşteriAdmin)

# Register your models here.
