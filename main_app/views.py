from django.shortcuts import render
from django.http import HttpResponse
from .models import drummers as drummers
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello! And welcome to Drummers Collector!</h1>")

def about(request):
    return render(request, "about.html")

def drummers_index(request):
    return render(request, "drummers/index.html", { "drummers": drummers})
    