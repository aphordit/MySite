from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage

def usermanager(request):
    
    return render(request, 'Back/usermanager.html')