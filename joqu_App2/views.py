from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    return HttpResponse("<center><h1>Hola Mundo! App2, Vista 1</h1></center>")

def vista2(request):
    return HttpResponse("<center><h1>Hola Mundo! App2, Vista 2</h1></center>")