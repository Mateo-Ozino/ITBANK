from django.shortcuts import render
from .forms import Form_prestamo
from django.contrib.auth.models import User
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def prestamos(request):
    
    user = Cliente.objects.get(customer_dni=User.get_username(request.user))
    
    formulario_inicial = Form_prestamo
    
    tipo_cliente = user.client_type
    
    customerID = user.customer_id
    
    cuenta = Cuenta.objects.filter(customer_id=customerID)
    cuenta = cuenta.filter(account_id=cuenta[0].account_id)

    match tipo_cliente:
        case 'CLASSIC':
            limite_prestamo = 100000
        case 'GOLD':
            limite_prestamo = 300000
        case 'BLACK':
            limite_prestamo = 500000
    
    if request.method == 'POST':
        formulario = Form_prestamo(request.POST)
        if formulario.is_valid():
            tipo_prestamo = formulario.cleaned_data['tipo_prestamo']
            fecha_inicio = formulario.cleaned_data['fecha_inicio']
            monto = formulario.cleaned_data['monto']
            if monto >= limite_prestamo:
                return render(request, 'prestamos/prestamos.html', {'formulario': formulario_inicial, 'error': True})
            else:
                nuevo_balance = cuenta[0].balance + monto
                cuenta.update(balance=nuevo_balance)

                Prestamo.objects.create(loan_type=tipo_prestamo, loan_date=fecha_inicio, loan_total=monto, customer_id = customerID)
                return render(request, 'prestamos/prestamos.html', {'formulario': formulario_inicial, 'success': True})
    
    return render(request, 'prestamos/prestamos.html', {'formulario': formulario_inicial})