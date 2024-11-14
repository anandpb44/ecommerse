from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Product
# Create your views here.

#------------LOGIN--------------
def eapp_login(req):
    if 'shop' in req.session:
        return redirect(eapp_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        shop=authenticate(username=uname,password=password)
        if shop:
            login(req,shop)
            req.session['shop']=uname
            return redirect(eapp_home)
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
        