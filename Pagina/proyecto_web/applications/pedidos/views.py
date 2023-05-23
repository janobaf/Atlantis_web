from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import  View,TemplateView
from django.views.generic.edit import (
    FormView,
   
)
from ..Mesas.models import mesa

from ..platos.models import Platos
from .models import PlatoPedidos,pedidos
from .forms import CreacionPlatosForm,CreacionPedidosForm
from ..usuarios.mixins import(AdministradorPermisionMixin,MeseroPermisionMixin,CocineroPermisionMixin)

class CreacionPedidosView(MeseroPermisionMixin,TemplateView):
    template_name="pedidos/addpedidos.html"
    success_url ="/" 

    def post(self, request, *args, **kwargs):
        mesa_aux=mesa.objects.filter(numero_mesa=self.kwargs['numero_mesa'])
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
        
        #platos=self.kwargs['id']
        platos=self.kwargs['pk']
        cantidad=self.request.POST.get('cantidad','')
       # platos=Platos.objects.get(id=self.kwargs['id_plato'])
        #pedido=pedidos.objects.get(id=self.kwargs['id_pedido'])
        print(platos,cantidad)
        return HttpResponseRedirect(
            reverse(
                'platos_app:list-platos'
            )
        )
