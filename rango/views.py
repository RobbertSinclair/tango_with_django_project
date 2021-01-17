from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #Context for the template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    
    return render(request, 'rango/index.html', context=context_dict)

def rango_app(request):
    return HttpResponse("Rango says wow you are in the rango app :)")

def rango_about(request):

    context = {"name": "Robbert Sinclair"}
    return render(request, "rango/about.html", context=context)


