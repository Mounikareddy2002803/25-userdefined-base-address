from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mouni(request):
    return HttpResponse('This is user defined base address')