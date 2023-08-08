from django.urls import path

from django.contrib.auth import views as auth_views

from SpareApp import views

urlpatterns = [
    path('', views.index, name='index'),
   
    
    #home page
    path('home/', views.home, name='home'),
    path('about', views.about, name='about'),
    path('home/<int:product_id>', views.product_detail, name='product_detail'),
    
    
    
    
    #Login path 
    path('login/', auth_views.LoginView.as_view(template_name='spare/login.html'), name= 'login'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name='spare/index.html'), name= 'logout'),
    
    
    
]
