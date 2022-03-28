from django.shortcuts import render,redirect
from django.http.response import HttpResponse

from django.contrib.auth import authenticate,login,logout



def login_view(request):
    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username =username1,password = password1)
        if user is not None:
            return redirect('home')
        else:
            return HttpResponse('invalid user')
    return render(request,'login.html')



def loguot_view(request):

    logout(request)
    return HttpResponse('loguot successfull')
    return redirect('login')


def home_view(request):
    return render(request,'home_page.html')
