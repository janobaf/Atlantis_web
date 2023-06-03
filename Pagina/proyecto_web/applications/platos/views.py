from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import(ListView)
from django.views.generic.edit import (FormView)
from .models import Platos
from .forms import CreacionPlatosForm
from ..usuarios.mixins import AdministradorPermisionMixin,MeseroPermisionMixin
from ..pedidos.models import pedidos
from django.db.models  import Value, IntegerField
# Create your views here.
class PlatosAddView(AdministradorPermisionMixin,FormView):
    template_name="platos/platosadd.html"
    form_class=CreacionPlatosForm
    success_url="/"
    
    def form_valid(self, form) :

        Platos.objects.CreatePlatosAdd(
            form.cleaned_data['id'],
            form.cleaned_data["Nombre_plato"],
            form.cleaned_data["precio_plato"],
            form.cleaned_data["categoria"],
            form.cleaned_data["imagen"]
        )
        
        return HttpResponseRedirect(
            reverse(
                'platos_app:list-platos',
               
            )
        )

    
class ListarPlatosView(MeseroPermisionMixin,ListView):
    template_name="platos/list-platos.html"
    model=Platos
    context_object_name= 'plato'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        if self.kwargs:
            id_pedido=self.kwargs['idpedido']
            context['idpedido'] = id_pedido
            pedido=pedidos.objects.get(id=id_pedido)
            print(pedido.plato)
            context['pedidos']= pedido
        return context    


    def get_queryset(self):
        categoria=self.request.GET.get('categoria','')
        
        queryset=Platos.objects.ListPlatosCategoria(categoria)
        return queryset
