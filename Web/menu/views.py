from django.shortcuts import get_object_or_404, redirect, render
from .models import Menu


# Create your views here.

def menu_add(request):

    return render(request, 'Back/menu_add.html')
