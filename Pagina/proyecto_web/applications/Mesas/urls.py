from django.urls import path

from . import views

app_name = "mesas_app"

urlpatterns = [
    path(
        'mesasadd/', 
        views.AddMesaView.as_view(),
        name='add-mesas',
    )
]