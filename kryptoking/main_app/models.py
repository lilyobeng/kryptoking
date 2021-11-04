
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    topic = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
    
    def get_absolute_url(self):
        return reverse('post_index')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.body


