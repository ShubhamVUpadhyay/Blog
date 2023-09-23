from django.urls import path
from Blog import views
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('details/<int:pk>/',views.ProdDetailView.as_view(),name='details'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('login/', views.login_view, name='login'),
]
