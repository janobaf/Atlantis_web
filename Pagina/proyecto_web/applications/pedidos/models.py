from django.db import models
from ..Mesas.models import mesa
from ..platos.models import Platos
from .managers import (PlatoManager,PedidosManager)
# Create your models here.
class PlatoPedidos(models.Model):
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    observacion = models.CharField(max_length=150)
    objects=PlatoManager()

    def get_nombre_plato(self):
        return self.plato.Nombre_plato
    def __str__(self):
        return self.plato.Nombre_plato
class pedidos(models.Model):
    id = models.AutoField(primary_key=True)
    mesa = models.OneToOneField(mesa,unique=True, on_delete=models.CASCADE)
    plato = models.ManyToManyField(PlatoPedidos,blank=True)
    precio_total = models.IntegerField(blank=True,null=True)
    objects=PedidosManager()
    
    