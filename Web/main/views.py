from django.shortcuts import get_object_or_404 , redirect , render 
from .models import Main


# Create your views here.

def home (request) :
    return render (request , 'home.html')
