from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Blog(models.Model):
    blog_title=models.CharField(max_length=200)
    blog_text=HTMLField()


