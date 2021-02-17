from django.db import models

class MüşteriModel(models.Model):
    isim=models.CharField(max_length=15)
    soyisim=models.CharField(max_length=15)
    eposta=models.EmailField()
    adres=models.TextField()

    class Meta():
        db_table="Müşteri"
        verbose_name="Müşteri"
        verbose_name_plural="Müşteriler"
    
    def __str__(self):
        return self.eposta