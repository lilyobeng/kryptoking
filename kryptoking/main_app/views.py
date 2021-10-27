
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Krypto


from bs4 import BeautifulSoup

import requests
import time

# Create your views here.

class KryptoCreate(CreateView):
   model = Krypto
   fields = ['name', 'price', 'information', 'symbol']

   def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class KryptoUpdate(UpdateView):
  model = Krypto
  fields = ['name', 'price', 'information', 'symbol']

class KryptoDelete(DeleteView):
  model = Krypto
  success_url = '/krypto/mykrypto/'

def home(request):
    return render(request, 'home.html')

def krypto_index(request):
    return render(request, 'krypto/index.html')

def my_krypto_index(request):
    krypto = Krypto.objects.all()
    return render(request, 'krypto/mykrypto.html', {'krypto': krypto})

def krypto_detail(request,krypto_id):
    krypto = Krypto.objects.get(id=krypto_id)
    return render(request, 'krypto/detail.html', {'krypto': krypto})




def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



  #program to get the current price of crypto

#Get the price of crypto:

url = 'https://www.google.com/search?q=bitcoin+price'


# Make a request to the website:

HTML = requests.get(url)

#Parse the HTML

soup = BeautifulSoup(HTML.text, 'html.parser')

#print soup to find where the text is that contains the price of the cryptocurrency

print(soup.prettify())