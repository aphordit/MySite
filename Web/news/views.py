from django.shortcuts import get_object_or_404 , redirect , render 
from .models import News


# Create your views here.

def news_add (request) :
    
    return render (request , 'news_add.html' )
