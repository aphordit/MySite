from django.shortcuts import get_object_or_404, redirect, render
from .models import Slide


# Create your views here.

def slide_add(request):

    return render(request, 'slide_add.html')
