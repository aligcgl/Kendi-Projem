
from django.db import models
from uygulama.models.kategori_model import KategoriModel
from django.db.models.fields.related import ManyToManyField

class ÜrünModel(models.Model):
    ürün_adı=models.CharField(max_length=20,null=True)
    fiyat=models.IntegerField()
    kategori=ManyToManyField(KategoriModel, related_name="ürünler")
    stok_adet=models.IntegerField()
    resim=models.ImageField(upload_to='ürün_resimleri', null=True, blank=True)

    class Meta():
        db_table="ürün"
        verbose_name="Ürün"
        verbose_name_plural="Ürünler"

    def __str__(self):
        return self.ürün_adı

