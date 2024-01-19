from django.shortcuts import render
from django.http import HttpResponse

def index(requesst):
    return HttpResponse("Rango says hey there partner!")

