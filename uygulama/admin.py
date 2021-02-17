from django.contrib import admin

from uygulama.models.müşteri_model import MüşteriModel
from uygulama.models.kategori_model import KategoriModel
from uygulama.models.ürün_model import ÜrünModel
from uygulama.models.spariş_model import SparişModel

class MüşteriAdmin(admin.ModelAdmin):
    search_fields=("isim","soyisim")
    list_display=("isim", "soyisim","eposta")

admin.site.register(MüşteriModel,MüşteriAdmin)

class KategoriAdmin(admin.ModelAdmin):
    search_fields=("kategori_name",)
    list_display=("kategori_name",)

admin.site.register(KategoriModel,KategoriAdmin)    


class ÜrünAdmin(admin.ModelAdmin):
    search_fields=("ürün_adı","kategori")
    list_display=("ürün_adı",)

admin.site.register(ÜrünModel,ÜrünAdmin)


class SparişAdmin(admin.ModelAdmin):
    search_fields=("ürün_adı","kategori")
    list_display=("müşteri","tutar")

admin.site.register(SparişModel,SparişAdmin)
