from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    return HttpResponse("<h1>Hola Mundo! Vista 1 App1 </h1>")

def vista2(request):
    return HttpResponse("<h1>Hola Mundo! Vista 2 App1 </h1>")
    
