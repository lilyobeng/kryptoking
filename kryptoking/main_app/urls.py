from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('krypto/', views.krypto_index, name='index'),
   path('krypto/mykrypto/', views.my_krypto_index, name='my_kyrpto_index'),
   path('krypto/<int:krypto_id>/', views.krypto_detail, name='detail'),
   path('krypto/create/', views.KryptoCreate.as_view(), name='krypto_create'),
   path('krypto/<int:pk>/update/', views.KryptoUpdate.as_view(), name='krypto_update'),
   path('krypto/<int:pk>/delete/', views.KryptoDelete.as_view(), name='krypto_delete'),
   path('accounts/signup/', views.signup, name='signup'),
]

