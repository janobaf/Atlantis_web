from django.urls import path

from . import views

app_name = "pedidos_app"

urlpatterns = [
    path(
        'pedidos-add/<numero_mesa>', 
        views.CreacionPedidosView.as_view(),
        name='add-pedidos',
    ),
    path(
        'pedidos-add-platos/<pk>/',
        views.AgregarPedidoView.as_view(),
        name="pedidos-add-platos"
    )
]