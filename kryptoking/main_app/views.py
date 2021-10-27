from django.shortcuts import render
from .models import Krypto

# Create your views here.
def home(request):
    return render(request, 'home.html')

def krypto_index(request):
    return render(request, 'krypto/index.html')

def my_krypto_index(request):
    kryptos = Krypto.objects.all()
    return render(request, 'krypto/mykrypto.html')