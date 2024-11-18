from django.urls import path,include
from eapp import views

urlpatterns=[
    path('',views.eapp_login),
    path('logout',views.eapp_logout),
    path('shop_home',views.eapp_home),
    path('shop_product',views.product),
    path('shop_edit/<id>',views.edit_pro),
    path('shop_delete/<pid>',views.delete),
    #---user--------
    path('user_reg',views.register),
    path('user_home',views.user_home)
    
]