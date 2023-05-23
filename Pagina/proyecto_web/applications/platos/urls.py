from django.urls import path

from . import views

app_name = "platos_app"

urlpatterns = [
    path(
        'platosadd/', 
        views.PlatosAddView.as_view(),
        name='add-platos',
    ),
    path('list-platos/',
         views.ListarPlatosView.as_view(),
         name='list-platos'
         ),
    path('list-platos-pedido/<idpedido>',
         views.ListarPlatosView.as_view(),
         name='list-platos-pedido'
         )
]