from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner!")

def rango_app(request):
    return HttpResponse("Rango says wow you are in the rango app :)")


