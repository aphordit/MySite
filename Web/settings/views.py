from django.shortcuts import get_object_or_404, redirect, render
from .models import Settings


# Create your views here.

def settings_add(request):

    return render(request, 'Back/settings_add.html')
