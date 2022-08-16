from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models as cliente_models
from django.contrib.auth.models import User
from Cuentas.models import Cuenta
from Tarjetas.models import Tarjeta

# Create your views here.
@login_required
def homebanking(request):
    user = cliente_models.Cliente.objects.get(customer_dni=User.get_username(request.user))
    customerID = user.customer_id
    cuenta = Cuenta.objects.filter(customer_id=customerID)
    tarjetas = Tarjeta.objects.filter(customer_id=customerID)
    marcas_tarjetas = [tarjeta.brand.capitalize() for tarjeta in tarjetas]
    context = {
        "cuenta": cuenta,
        "tarjetas": tarjetas,
        "marcas_tarjetas": marcas_tarjetas,
    }
    return render(request, 'Clientes/homebanking.html', context)