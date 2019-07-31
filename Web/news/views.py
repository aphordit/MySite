from django.shortcuts import get_object_or_404, redirect, render
from .models import News


# Create your views here.

def news_add(request):

    return render(request, 'Back/news_add.html')


def news(request):

    news = News.objects.all().order_by('-pk')
    print(news)
    return render(request, 'Front/news.html', {'news': news})
