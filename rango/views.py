from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #Context for the template
    context_dict = {"boldmessage": "Cool message"}
    


    return render(request, "rango/index.html", context=context_dict)

def rango_app(request):
    return HttpResponse("Rango says wow you are in the rango app :)")

def rango_about(request):
    return HttpResponse("<h1>Rango says here is the about page <a href='http://127.0.0.1:8000'>Go back</a></h1>")


