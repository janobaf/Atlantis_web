# Generated by Django 4.1.8 on 2023-05-19 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre_plato', models.CharField(max_length=150, verbose_name='Nombre_Plato')),
                ('precio_plato', models.FloatField(verbose_name='precio_plato')),
                ('categoria', models.CharField(choices=[('0', 'Criollos'), ('1', 'Ceviches'), ('2', 'Especialidades'), ('3', 'Chicharrones'), ('4', 'Parrillas'), ('5', 'postres'), ('6', 'Gaseosas'), ('7', 'TAPERS')], max_length=1, verbose_name='Categoria')),
                ('imagen', models.ImageField(upload_to='platos')),
            ],
        ),
    ]
