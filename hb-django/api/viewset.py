from Clientes.models import Cliente, Sucursal, Direccion
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from Tarjetas.models import Tarjeta
from api.serializers import ClienteSerializer, CuentaSerializer, UserSerializer, PrestamoSerializer, TarjetaSerializer, SucursalSerializer, DireccionSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from itertools import chain
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = 'customer_dni'
    
    def retrieve(self, request, customer_dni):
        queryset = Cliente.objects.all()
        cliente = get_object_or_404(queryset, customer_dni=customer_dni)
        serializer = ClienteSerializer(cliente, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['GET'], url_name='tarjetas', url_path='tarjetas')
    def tarjetas(self, request, customer_dni):
        tarjetas = Tarjeta.objects.filter(customer_id=Cliente.objects.get(customer_dni=customer_dni).customer_id)
        serializer = TarjetaSerializer(tarjetas, many=True, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'], url_name='modificar_direccion', url_path='modificar_direccion')
    def modificar_direccion(self, request, customer_dni):
        direccion = Cliente.objects.get(customer_dni=customer_dni).direccion
        serializer = DireccionSerializer(direccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'tarjetas':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class CuentaViewSet(viewsets.ViewSet):
    lookup_field = 'customer_dni'
    
    def list(self, request):
        queryset = Cuenta.objects.all()
        serializer = CuentaSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, customer_dni):
        cuenta = Cuenta.objects.filter(customer_id=Cliente.objects.get(customer_dni=customer_dni).customer_id)
        serializer = CuentaSerializer(cuenta, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class TarjetaViewSet(viewsets.ViewSet):
    lookup_field = 'customer_dni'
    permission_classes = [permissions.IsAdminUser]

    def list(self, request):
        queryset = Tarjeta.objects.all()
        serializer = TarjetaSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, customer_dni):
        tarjetas = Tarjeta.objects.filter(customer_id=Cliente.objects.get(customer_dni=customer_dni).customer_id)
        serializer = TarjetaSerializer(tarjetas, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PrestamoViewSet(viewsets.ModelViewSet):
    lookup_field = 'customer_dni'
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    
    def list(self, request):
        queryset = Prestamo.objects.all()
        serializer = PrestamoSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, customer_dni):
        prestamo = Prestamo.objects.filter(customer_id=Cliente.objects.get(customer_dni=customer_dni).customer_id)
        serializer = PrestamoSerializer(prestamo, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='generar', url_name='generar')
    def generar_prestamo(self, request, customer_dni):
        cuenta = Cuenta.objects.filter(customer_id=Cliente.objects.get(customer_dni=customer_dni).customer_id)
        serializer = PrestamoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            nuevo_balance = cuenta[0].balance + request.data["loan_total"]
            cuenta.update(balance=nuevo_balance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['delete', 'get'], url_path='anular', url_name='anular')
    def anular_prestamo(self, request, customer_dni):
        cuenta = Cuenta.objects.filter(customer_id=Cliente.objects.get(customer_dni=customer_dni).customer_id)
        prestamo = list(Prestamo.objects.filter(customer_id = cuenta[0].customer_id))[-1]
        nuevo_balance = cuenta[0].balance - prestamo.loan_total
        cuenta.update(balance=nuevo_balance)
        prestamo.delete()
        return Response('Prestamo anulado')

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    
    @action(detail=True, methods=['GET'], url_path='prestamos', url_name='prestamos', permission_classes=[permissions.IsAdminUser])
    def prestamo_por_sucursal(self, request, pk):
        clientes = Cliente.objects.filter(branch_id=pk)
        resultado = []
        for cliente in clientes:
            prestamos = Prestamo.objects.filter(customer_id=cliente.customer_id)
            resultado = chain(resultado, prestamos)
        serializer = PrestamoSerializer(resultado, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DireccionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer