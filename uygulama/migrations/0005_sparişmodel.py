# Generated by Django 3.1.6 on 2021-02-17 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uygulama', '0004_ürünmodel_resim'),
    ]

    operations = [
        migrations.CreateModel(
            name='SparişModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutar', models.IntegerField()),
                ('kategori', models.ManyToManyField(related_name='sparişler', to='uygulama.KategoriModel')),
                ('müşteri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sparişler', to='uygulama.müşterimodel')),
                ('ürün', models.ManyToManyField(related_name='sparişler', to='uygulama.ÜrünModel')),
            ],
            options={
                'verbose_name': 'Spariş',
                'verbose_name_plural': 'Sparişler',
                'db_table': 'spariş',
            },
        ),
    ]
