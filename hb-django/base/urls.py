from django.urls import path
from . import views
from Clientes import views as clientes_views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('homebanking/', clientes_views.homebanking, name='homebanking'),
    path('preHomebanking/', views.preHomebanking, name='preHomebanking'),
]