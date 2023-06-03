from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import  View,TemplateView
from django.views.generic.edit import (
    FormView
)
from .models import PlatoPedidos,pedidos
from ..Mesas.models import mesa
from ..platos.models import Platos
from ..usuarios.mixins import(AdministradorPermisionMixin,MeseroPermisionMixin,CocineroPermisionMixin)

class CreacionPedidosView(MeseroPermisionMixin,TemplateView):
    template_name="pedidos/addpedidos.html"
    success_url ="/" 

    def post(self, request, *args, **kwargs):
        mesa_aux=mesa.objects.filter(numero_mesa=self.kwargs['numero_mesa'])
        if mesa_aux.count()>0:
            try:
                pedido_aux = pedidos.objects.get(mesa=mesa_aux[0])
                return HttpResponseRedirect(
                    reverse(
                        'platos_app:list-platos-pedido',
                        kwargs={'idpedido':pedido_aux.id}
                    )
                )
            except:
                pedido=pedidos.objects.addPedidos(
                    mesa=mesa_aux[0]
                )
                return HttpResponseRedirect(
                    reverse(
                        'platos_app:list-platos-pedido',
                        kwargs={'idpedido':pedido.id}
                    )
                )
        

class AgregarPedidoView(MeseroPermisionMixin,View):

    def post(self,request,*args,**kwargs):
        
        platos_id=self.kwargs['pk']
        pedido_id=self.kwargs['idpedido']
        cantidad=self.request.POST.get('cantidad','')
        observaciones = self.request.POST.get('observaciones','')
        plato = Platos.objects.get(id=platos_id)
        if not observaciones:
            plato_pedidos = PlatoPedidos.objects.addPlatoPedidos(
                plato=plato,
                cantidad=cantidad
            )
        else:
            plato_pedidos = PlatoPedidos.objects.addPlatoPedidos(
                plato=plato,
                cantidad=cantidad,
                observaciones=observaciones
            )
        pedido = pedidos.objects.get(id=pedido_id)
        precio_total=pedido.precio_total+(plato.precio_plato*float(cantidad))
        pedido.plato.add(plato_pedidos)
        pedido.precio_total=precio_total
        pedido.save()
    
        return HttpResponseRedirect(
            reverse(
                'platos_app:list-platos-pedido',
                kwargs={'idpedido':pedido_id}
            )
        )
