from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('krypto/', views.krypto_index, name='index'),
   path('post/', views.post_index, name='post_index'),
   path('post/<int:post_id>/', views.post_detail, name='detail'),
   path('post/create/', views.PostCreate.as_view(), name='post_create'),
   path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
   path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
   path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
   path('accounts/signup/', views.signup, name='signup'),
]

