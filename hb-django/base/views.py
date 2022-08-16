from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def nosotros(request):
    return render(request, 'base/nosotros.html')

def ayuda(request):
    return render(request, 'base/ayuda.html')

def preHomebanking(request):
    return render(request, 'base/preHomebanking.html')

