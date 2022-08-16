from django import forms
from django.contrib.auth.models import User

# class DateInput(forms.DateInput):
#     input_type = 'date'

class Form_prestamo(forms.Form):
    tipo_prestamo = forms.ChoiceField(choices=(('PERSONAL', 'Prestamo personal'), ('HIPOTECARIO', 'Prestamo hipotecario'), ('PRENDARIO', 'Prestamo prendario')), label='Tipo de prestamo', required=True, widget=forms.Select(attrs={'class':'form-control mb-1'}))
    
    fecha_inicio = forms.DateField(label='Fecha de inicio', input_formats=['%Y-%m-%d'], required=True, widget=forms.DateInput(attrs={'class':'form-control mb-1', 'type':'date'}))
    
    monto = forms.DecimalField(label='Monto', min_value=0, required=True, widget=forms.NumberInput(attrs={'class':'form-control mb-1'}))

