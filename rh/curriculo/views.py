from django.shortcuts import render

# Create your views here.

def home(request, **kwargs):
    return (request. 'home.html', {})