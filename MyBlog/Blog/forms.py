from django import forms
from .models import BlogPost,Userinfo,AuthorizationRequest
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
#---------------------------------Models-------------------------------------------------------------
class postCreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('blog_title','blog_text')

class UserinfoForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    conf_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Confirm Password")
    bio=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),required=False)
    
    class Meta():
        model=User
        fields=['username','first_name','last_name','email','bio','password']
    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        conf_password=self.cleaned_data.get('conf_password')
        if password != conf_password:
            raise forms.ValidationError("Password do not macth")
        return conf_password
class UserinfoUpdateForm(forms.ModelForm):
    first_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = Userinfo
        fields = ['first_name', 'last_name', 'email']
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label="Old Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label="New Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
class AuthorizationForm(forms.ModelForm):
    name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    message=forms.CharField(label='Your Message',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Describe Why You want Authorship...'}),max_length=500)
    class Meta:
        model=AuthorizationRequest
        fields=['name','email','message']
class ContactForm(forms.Form):
    name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
#---------xxxxxxxxxxxxxxx------------------------Models----------------------xxxxxxxxxxxxxxxxxxxx----