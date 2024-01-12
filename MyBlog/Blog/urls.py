from django.urls import path
from Blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomPasswordChangeForm
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('details/<int:pk>/',views.ProdDetailView.as_view(),name='details'),
    path('update/<int:pk>/',views.updatePostView.as_view(),name='update'),
    path('delete/<int:pk>/',views.deletePostView.as_view(),name='delete'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/',views.ContactUs,name='contact'),
    path('myposts/',views.UserPostListView.as_view(),name='myposts'),
    path('register/', views.signup_view,name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-pass/',PasswordChangeView.as_view(
        template_name = 'accounts/change-pass.html',
        success_url = '/profile/',
        form_class= CustomPasswordChangeForm,
        ),name='change-pass'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('create/', views.createPostView.as_view(), name='create'),
    path('profile/', views.profile_view, name='profile'),
    path('req-author/', views.request_authorization,name='req-author'),
    path('search/', views.blog_search, name='blog_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
