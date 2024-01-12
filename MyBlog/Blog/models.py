from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
class Userinfo(models.Model):
    user=models.OneToOneField(User, on_delete=callable)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    bio=models.CharField(max_length=250)
    profile_img=models.ImageField(upload_to="profiles/",blank=True,null=True)
class BlogPost(models.Model):
    blog_title=models.CharField(max_length=200)
    blog_text=HTMLField()
    creation_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
class AuthorizationRequest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,default=None)
    email=models.EmailField()
    message=models.TextField()
    is_approved=models.BooleanField(default=False)
