from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def eapp_login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        shop=authenticate(username=uname,password=password)
        if shop:
            login(req,shop)
            return redirect(eapp_home)
        else:
            return redirect(eapp_login)
    else:
        return render(req,'login.html')
    
def eapp_logout(req):
    logout(req)
    return redirect(eapp_login)

def eapp_home(req):
    return render(req,'shop/home.html')

