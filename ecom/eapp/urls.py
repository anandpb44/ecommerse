from django.urls import path,include
from eapp import views

urlpatterns=[
    path('',views.eapp_login),
    path('logout',views.eapp_logout),
    path('shop_home',views.eapp_home),
    path('shop_product',views.product),
    
]