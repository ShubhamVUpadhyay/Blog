from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import BlogPost,AuthorizationRequest,Userinfo
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView,ListView,TemplateView,CreateView,UpdateView,DeleteView
from .forms import postCreateForm,UserinfoForm,AuthorizationForm,CustomPasswordChangeForm,UserinfoUpdateForm,ContactForm
from  django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
class IndexView(ListView):
    model=BlogPost
    template_name='MyBlog/index.html'
    context_object_name='blog' 
class UserPostListView(ListView):
    model=BlogPost
    template_name='MyBlog/user_post.html'
    context_object_name='post'
    def get_queryset(self):
        user=self.request.user
        return BlogPost.objects.filter(author=user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authorization_request = AuthorizationRequest.objects.filter(user=self.request.user).first()
        context['authorization_request'] = authorization_request
        return context
class ProdDetailView(DetailView):
    model=BlogPost
    template_name='MyBlog/details.html'
    context_object_name='blog'
class AboutView(TemplateView):
    template_name='MyBlog/about.html'
class createPostView(CreateView):
    model=BlogPost
    form_class=postCreateForm
    template_name='MyBlog/create-post.html'
    success_url=reverse_lazy('myposts')
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class updatePostView(UpdateView):
    model=BlogPost
    form_class=postCreateForm
    template_name='MyBlog/create-post.html'
    success_url=reverse_lazy('myposts')    
class deletePostView(DeleteView):
    model=BlogPost
    template_name='MyBlog/confirm_delete.html'
    success_url=reverse_lazy('myposts')

def signup_view(request):
    registered=False
    if request.method == 'POST':
        user_form=UserinfoForm(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            return HttpResponse(user_form.errors)
    else:
        user_form=UserinfoForm()
    return render(request,'accounts/Signup.html',{'fn':user_form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'accounts/login.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
@login_required
class ChangePassView(PasswordChangeView):
    template_name = 'accounts/change-pass.html'
    success_url = reverse_lazy('profile')
    form_class= CustomPasswordChangeForm
@login_required
def profile_view(request):
    authorization_request = AuthorizationRequest.objects.filter(user=request.user).first()
    return render(request,'accounts/profile.html',{'authorization_request': authorization_request})

@login_required
def request_authorization(request):
     authorization_request = AuthorizationRequest.objects.filter(user=request.user).first()
     if request.method == 'POST':
        form=AuthorizationForm(data=request.POST,instance=authorization_request)
        if form.is_valid():
            author_req=form.save(commit=False)
            author_req.user=request.user
            author_req.save()
        else:
            return HttpResponse(form.errors)
     else:
        form=AuthorizationForm(instance=authorization_request)
     return render(request,'accounts/authorization_request.html',{'fn':form,'authorization_request':authorization_request})


@login_required
def update_profile(request):
    user_info = request.user
    if request.method == 'POST':
        form = UserinfoUpdateForm(request.POST, request.FILES, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = UserinfoUpdateForm(instance=user_info)

    return render(request, 'accounts/update-profile.html', {'form': form})

def ContactUs(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            email_msg=f'Name:{name}\n'
            email_msg+=f'Email:{email}\n'
            email_msg+=f'Message:{message}'
            send_mail(
                'Contact Us',
                email_msg,
                settings.EMAIL_HOST_USER,
                ['shubhamvupadhyay@gmail.com'],
                fail_silently=False,
            )
            msg=messages.success(request,"Email Sent Succesfully")
            return redirect('index')
    else:
        form=ContactForm()
    return render(request,'accounts/contact-page.html',{'form':form})
def blog_search(request):
    query = request.GET.get('search', '') 
    blog_posts = BlogPost.objects.filter(blog_title__icontains=query)  
    return render(request, 'MyBlog/search_results.html', {'query': query, 'blog_posts': blog_posts})