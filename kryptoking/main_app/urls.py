from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('krypto/', views.krypto_index, name='index'),
   path('comment/', views.comment_index, name='comment_index'),
   path('comment/create/', views.CommentCreate.as_view(), name='comment_create'),
   path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
   path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
   path('accounts/signup/', views.signup, name='signup'),
]

