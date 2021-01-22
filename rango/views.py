from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    
    return HttpResponse("Rango greets you! See also: <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("<a href='/rango/'>Back</a> This is Rango's about page!")