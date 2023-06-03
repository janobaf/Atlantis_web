# Generated by Django 4.1.8 on 2023-06-02 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('platos', '__first__'),
        ('Mesas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatoPedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('observacion', models.CharField(max_length=150)),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platos.platos')),
            ],
        ),
        migrations.CreateModel(
            name='pedidos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('precio_total', models.IntegerField(blank=True, null=True)),
                ('mesa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Mesas.mesa')),
                ('plato', models.ManyToManyField(blank=True, to='pedidos.platopedidos')),
            ],
        ),
    ]
