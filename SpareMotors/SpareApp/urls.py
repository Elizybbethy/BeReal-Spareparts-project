from django.urls import path

from django.contrib.auth import views as auth_views

from SpareApp import views

urlpatterns = [
    path('', views.index, name='index'),
   
    
    #home page
    path('home/', views.home, name='home'),
    path('about', views.about, name='about'),
    path('home/<int:product_id>', views.product_detail, name='product_detail'),
    
    #All sales made
    path('all_sales/', views.all_sales, name='all_sales'),
    path('issue_item/<str:pk>', views.issue_item, name='issue_item'),
    
    #Add to stock
    path('add_to_stock/<str:pk>', views.add_to_stock, name="add_to_stock"),
    
    #Receipt url
    path('receipt', views.receipt, name='receipt'),
    path('receipt/<int:receipt_id>', views.receipt_detail, name='receipt_detail'),
    
    
    #category
    path('category/', views.category, name='category'),
    
    #Login path 
    path('login/', auth_views.LoginView.as_view(template_name='spare/login.html'), name= 'login'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name='spare/index.html'), name= 'logout'),
    
    
    
]
