from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def logout(request):
    del(request.session['user'])
    return redirect('/')

def login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form':form})
        
def register(request):
    if request.method =="GET":
        return render(request, 'users/register.html')
    elif request.method=="POST":
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        res_msg = {}
        if not (username and useremail and password and re_password):
            res_msg['error'] = "모든 값을 입력해주세요."
        elif password != re_password:
            res_msg['error'] = "비밀번호가 일치하지 않습니다."
        #이미 존재하는 아이디 처리.
        else:
            user = Users(
                username=username,
                useremail=useremail,    
                password = make_password(password)
            )
            user.save()

        return render(request, 'users/register.html', res_msg)