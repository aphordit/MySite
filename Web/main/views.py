from django.shortcuts import get_object_or_404 , redirect
from django.shortcuts import render
from .models import Main


# Create your views here.

def home (request) :
    return render (request , 'home.html')
