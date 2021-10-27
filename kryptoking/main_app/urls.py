from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('krypto/', views.krypto_index, name='index'),
   path('krypto/mykrypto/', views.my_krypto_index, name='my_kyrpto_index'),
]