from api.views import *
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'cuentas', CuentaViewSet, basename='cuenta')
router.register(r'prestamos', PrestamoViewSet, basename='prestamo')
router.register(r'tarjetas', TarjetaViewSet, basename='tarjeta')
router.register(r'sucursales', SucursalViewSet, basename='sucursal')
router.register(r'direcciones', DireccionViewSet)

urlpatterns = [ 
    path('', include(router.urls)), 
]