from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print("hello")
    return render(request, 'home.html')

def posts(request): 
    return HttpResponse('<h1>Test response</h1>')

def post(request, post_id): pass

def add_post(request): pass
