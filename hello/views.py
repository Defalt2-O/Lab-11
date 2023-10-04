from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'hello/index1.html')

def about(request):
    return render(request, 'hello/about.html')