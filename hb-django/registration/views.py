from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-1', 'placeholder':'DNI'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-1', 'placeholder':'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-1', 'placeholder':'Apellido'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-1', 'placeholder':'Correo electrónico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-1', 'placeholder':'Contraseña'})
        form.fields['password2'].widget= forms.PasswordInput(attrs={'class':'form-control mb-1', 'placeholder':'Repita la contraseña'})
        form.fields['username'].label = ''
        form.fields['first_name'].label = ''
        form.fields['last_name'].label = ''
        form.fields['email'].label = ''
        form.fields['password1'].label = ''
        form.fields['password2'].label = ''
        return form