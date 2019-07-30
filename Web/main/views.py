from django.shortcuts import get_object_or_404, redirect, render
from .models import Main
from news.models import News
from slide.models import Slide

# Create your views here.


def home(request):
    news = News.objects.all()
    slides = Slide.object.all()
    return render(request, 'home.html', {'news': news}, {'slides': slides})
