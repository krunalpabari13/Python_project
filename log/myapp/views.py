from django.shortcuts import render
import hashlib
from .models import registration
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from . import extract
def index(request):
    return render(request,'index.html')
@csrf_exempt
def checking(request):
    if request.method=='POST':
        data=request.body.decode('utf-8');
        jsondata=json.loads(data)
        
        extract.extract(jsondata);
    return render(request,'index.html')

def data(request):
    return render(request, 'data.html')
def auth_login_basic(request):
    return render(request,'auth-login-basic.html')

def auth_register_basic(request):
    return render(request, "auth-register-basic.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password = hashlib.sha256(password.encode()).hexdigest()
    try:
        user = registration.objects.get(email=email, password=password)
        request.session['id'] = user.id
        request.session['name']=user.name
        print('done')
        messages.success(request, "Log in successfull")
        return render(request, 'index.html')
    except:
        print("login failed")
        user = None
        messages.success(request, "Enter proper email and password")
        return render(request, 'auth-login-basic.html')
@csrf_exempt
def sign(request):
    if request.method=='POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        passwd = request.POST.get("password")
        passwd = hashlib.sha256(passwd.encode()).hexdigest()
        try:
            user = registration.objects.get(email=email)
            messages.success(request, "This email is already use")
            return render(request, 'auth-login-basic.html')
        except:
            query = registration(name=name, email=email, password=passwd, phone=phone)
            query.save()
            messages.success(request, "Registration done")
    return render(request,'auth-login-basic.html')

