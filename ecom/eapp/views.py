from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User
# Create your views here.

#------------LOGIN--------------
def eapp_login(req):
    if 'shop' in req.session:
        return redirect(eapp_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        shop=authenticate(username=uname,password=password)
        if shop:
            login(req,shop)
            if shop.is_superuser:
                req.session['shop']=uname
                return redirect(eapp_home)
            else:
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid user name or password')
            return redirect(eapp_login)
    else:
        return render(req,'login.html')

#-----------LOGOUT----------------=
#  
def eapp_logout(req):
    logout(req)
    req.session.flush()
    return redirect(eapp_login)

#-------------------------------------

#--------------ADMIN-------------------
def eapp_home(req):
    if 'shop' in req.session:
        product=Product.objects.all()
        return render(req,'shop/home.html',{'products':product})
    else:
        return redirect(eapp_login)
    
def product(req):
    if 'shop' in req.session:
        if req.method=='POST':
            pid=req.POST['id']
            name=req.POST['name']
            dis=req.POST['dis']
            price=req.POST['price']
            off_price=req.POST['offprice']
            stock=req.POST['stock']
            img=req.FILES['img']
            data=Product.objects.create(pid=pid,name=name,dis=dis,price=price,offer_price=off_price,stock=stock,img=img)
            data.save()
            return redirect(eapp_home)
        else:

            return render(req,'shop/product.html')
    else:
        return redirect(eapp_login)
def edit_pro(req,id):
    if req.method=='POST':
        pid=req.POST['id']
        name=req.POST['name']
        dis=req.POST['dis']
        price=req.POST['price']
        off_price=req.POST['offprice']
        stock=req.POST['stock']
        img=req.FILES.get('img')
        if img:
            Product.objects.filter(pk=id).update(pid=pid,name=name,dis=dis,price=price,offer_price=off_price,stock=stock)
            data=Product.objects.get(pk=id)
            data.img=img
            data.save()
        else:
            Product.objects.filter(pk=id).update(pid=pid,name=name,dis=dis,price=price,offer_price=off_price,stock=stock)
        return redirect(eapp_home)
    else:
        data=Product.objects.get(pk=id)
        return render(req,'shop/edit_product.html',{'data':data})
def delete(req,pid):
    data=Product.objects.get(pk=pid)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(eapp_home)

#********************************

#--------------USER-----------------
def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
            return redirect(eapp_login)
        except:
            messages.warning(req,'Email Already Exit')
            return redirect(register)
    else:
        return render(req,'user/register.html')
def user_home(req):
    if 'user' in req.session:
        product=Product.objects.all()
        return render(req,'user/user_home.html',{'products':product})
def user_view(req,id):
    data=Product.objects.get(pk=id)
    return render(req,'user/view_product.html',{'data':data})
#------------Add to cart----------
def add_cart(req,id):
    pro=Product.objects.get(pk=id)
    user=User.objects.get(username=req.session['user'])
    try:
        cart=Cart.objects.get(pro=pro,user=user)
        cart.qty+=1
        cart.save()
    except:
        data=Cart.objects.create(pro=pro,user=user,qty=1)
        data.save()
    return redirect(view_cart)

def view_cart(req):
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.filter(user=user)
    return render(req,'user/cart.html',{'cart':data})
def qty_incri(req,cid):
    data=Cart.objects.get(pk=cid)
    if data.pro.stock > data.qty:
        data.qty+=1
        data.save()
    return redirect(view_cart)
def qty_dec(req,cid):
    data=Cart.objects.get(pk=cid)
    data.qty-=1
    data.save()
    if data.qty==0:
        data.delete()
    return redirect(view_cart)

def user_buypro(req,pid):
    product=Product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    qty=1
    price=product.offer_price
    buy=Buy.objects.create(pro=product,user=user,qty=qty,t_price=price)
    return redirect(user_bookings)

def user_bookings(req):
    return render(req,'user/bookings.html')