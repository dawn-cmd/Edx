from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def jing(request):
    return HttpResponse("Hello Jing")


def venti(request):
    return HttpResponse("Hello, Venti")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
