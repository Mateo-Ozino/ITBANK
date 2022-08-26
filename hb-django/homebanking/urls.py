"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Prestamos import views as prestamos_views
from api import views as api_views
# from base import views as base_views
# from base import urls as base_urls

urlpatterns = [
    path('', include('base.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('prestamos/', prestamos_views.prestamos, name='prestamos'),
    path('api/', include('api.urls')),
    # path('api/clientes/', api_views.ClienteLists.as_view()),
    # path('api/clientes/<int:customer_dni>/', api_views.ClienteDetails.as_view()),
    # path('api/clientes/tarjetas/<int:customer_dni>', api_views.TarjetaLists.as_view()),
    # path('api/cuentas/<int:customer_dni>/', api_views.CuentaLists.as_view()),
    # path('api/users/', api_views.UserList.as_view()),
    # path('api/users/<int:pk>/', api_views.UserDetail.as_view()),
    # path('api/prestamos/<int:customer_dni>/', api_views.PrestamoLists.as_view()),
    # path('api/prestamos/sucursal/<int:branch_id>/', api_views.PrestamoSucursal.as_view()),
    # path('api/prestamos/generador/<int:customer_dni>/', api_views.GenerarPrestamo.as_view()),
    path('admin/', admin.site.urls),
]
