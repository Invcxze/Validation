from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .forms import UserSign

def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            login = userform.cleaned_data["login"]
            email = userform.cleaned_data["email"]
            password = userform.cleaned_data["password"]
            return HttpResponse(f''' {login}, Поздравляю с регистрацией! <br> 
            Указанные вами данные: <br>
             Логин - {login}, <br>
              Пароль - {password}, <br>
               Электронная почта -{email}''')
        return render(request, "index.html", {"form": userform})
    userform = UserForm()
    return render(request, "index.html", {"form": userform})

def login(request):
    if request.method == "POST":
        usersign = UserSign(request.POST)
        if usersign.is_valid():
            login = usersign.cleaned_data["login"]
            password = usersign.cleaned_data["password"]
            if login == 'User1' and password == '12345678':
                return HttpResponse(f'{login},Поздравляю с успешным входом')
            else:
                return redirect('SIGN UP')
        return render(request, "login.html", {"form": usersign})
    usersign = UserSign()
    return render(request, "login.html", {"form": usersign})
    