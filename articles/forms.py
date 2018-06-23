from django.forms import ModelForm
from . import models

class CreateArticles(ModelForm):
    class Meta:
        model=models.Articles
        fields=['title','text','slug','thumb']