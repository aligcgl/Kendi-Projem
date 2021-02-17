from django.db import models

class KategoriModel(models.Model):
    kategori_name=models.CharField(max_length=20)

    class Meta():
        db_table="kategori"
        verbose_name="Kategori"
        verbose_name_plural="Kategoriler"
    
    def __str__(self):
        return self.kategori_name


