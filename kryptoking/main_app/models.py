from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.



    

class Comment(models.Model):
    description = models.CharField(max_length=500)
    date = models.DateField('posted')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('comment_index', kwargs={'comment_id': self.id})