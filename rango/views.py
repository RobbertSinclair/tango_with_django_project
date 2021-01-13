from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='http://127.0.0.1:8000/rango/about/'>Click here to find out about me</a>")

def rango_app(request):
    return HttpResponse("Rango says wow you are in the rango app :)")

def rango_about(request):
    return HttpResponse("<h1>Rango says here is the about page <a href='http://127.0.0.1:8000'>Go back</a></h1>")


