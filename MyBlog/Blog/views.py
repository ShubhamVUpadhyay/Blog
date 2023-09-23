from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Blog
from django.views.generic import DetailView,ListView,TemplateView
class IndexView(ListView):
    model=Blog
    template_name='MyBlog/index.html'
    context_object_name='blog' 
class ProdDetailView(DetailView):
    model=Blog
    template_name='MyBlog/details.html'
    context_object_name='blog'
class AboutView(TemplateView):
    template_name='MyBlog/about.html'



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin:index')  # Redirect to the admin panel
    return render(request, 'accounts/login.html')
