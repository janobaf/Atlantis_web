from django.shortcuts import render
from .models import mesa
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import(ListView)
from django.views.generic.edit import (FormView)
from ..usuarios.mixins import AdministradorPermisionMixin,MeseroPermisionMixin
from .forms import CreateMesasForms
class AddMesaView(MeseroPermisionMixin,FormView):
    template_name="mesas/add-mesas.html"
    form_class=CreateMesasForms
    success_url="/"

    def form_valid(self, form):
        mesa.objects.createmesas(
            form.cleaned_data['numero_mesa']
            
        )   
 
        return HttpResponseRedirect(
            reverse(
                'pedidos_app:add-pedidos',
                kwargs={'numero_mesa': form.cleaned_data['numero_mesa']}
            )
        )

