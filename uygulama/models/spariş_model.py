from django.db import models
from django.db.models.fields import related
from django.db.models.fields.related import ManyToManyField
from django.db.models.fields.related import ForeignKey
from uygulama.models.kategori_model import KategoriModel
from uygulama.models.müşteri_model import MüşteriModel
from uygulama.models.ürün_model import ÜrünModel

class SparişModel(models.Model):
    kategori=ManyToManyField(KategoriModel, related_name="sparişler")
    müşteri=models.ForeignKey(MüşteriModel, on_delete=models.CASCADE,related_name="sparişler")
    ürün_adı=models.ForeignKey(ÜrünModel, on_delete=models.CASCADE,related_name="sparişler")
    tutar=models.IntegerField()

    class Meta():
        db_table= "spariş"
        verbose_name="Spariş"
        verbose_name_plural="Sparişler"

    