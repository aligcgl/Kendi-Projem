# Generated by Django 3.1.6 on 2021-02-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MüşteriModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=15)),
                ('soyisim', models.CharField(max_length=15)),
                ('eposta', models.EmailField(max_length=254)),
                ('adres', models.TextField()),
            ],
            options={
                'verbose_name': 'Müşteri',
                'verbose_name_plural': 'Müşteriler',
                'db_table': 'Müşteri',
            },
        ),
    ]
