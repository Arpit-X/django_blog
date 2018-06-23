from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default='default.jpg',blank=True)
    author=models.ForeignKey(to=User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:50]+"..."