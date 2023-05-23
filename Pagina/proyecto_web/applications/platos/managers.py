from django.db import models


class PlatosManager(models.Manager):

    def _createPlatos(self,id,Nombre_plato,precio_plato,categoria,imagen):
        platos=self.model(
            id=id,
            Nombre_plato=Nombre_plato,
            precio_plato=precio_plato,
            categoria=categoria,
            imagen=imagen
        )
        platos.save(using=self.db)
        return platos
    def CreatePlatosAdd(self,id,Nombre_plato,precio_plato,categoria,imagen):
        return self._createPlatos(id,Nombre_plato,precio_plato,categoria,imagen)
    
    def ListPlatosCategoria(self,categoria_aux):
        consulta=self.filter(categoria=categoria_aux)
        
        return consulta
    
