from django.shortcuts import render


# Create your views here.
def login_func(request):
    return render(request, "registration/login.html")