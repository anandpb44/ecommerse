from django.urls import path,include
from eapp import views

urlpatterns=[
    path('',views.eapp_login),
    path('logout',views.eapp_logout),


    #--------ADMIN------------

    path('shop_home',views.eapp_home),
    path('shop_product',views.product),
    path('shop_edit/<id>',views.edit_pro),
    path('shop_delete/<pid>',views.delete),
    path('bk',views.bookings),

    #---user--------
    path('user_reg',views.register),
    path('user_home',views.user_home),
    path('user_view/<id>',views.user_view),
    path('addcart/<id>',views.add_cart),
    path('viewcart',views.view_cart),
    path('incr/<cid>',views.qty_incri),
    path('decr/<cid>',views.qty_dec),
    path('buy/<pid>',views.user_buypro),
    path('booking',views.user_bookings),
    path('cart_buy/<cid>',views.cart_buy),
    
]