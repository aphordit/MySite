from django.shortcuts import get_object_or_404, redirect, render
from .models import Main
from news.models import News
from slide.models import Slide

# Create your views here.


def home(request):
    news = News.objects.all().order_by('-pk')[:3]
    slides = Slide.objects.all()
    return render(request, 'Front/home.html', {'news': news, 'slides': slides})


def dashboard(request):

    return render(request, 'Back/admin/dashbord.html')
