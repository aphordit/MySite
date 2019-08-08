from django.shortcuts import get_object_or_404, redirect, render
from .models import News


# Create your views here.

def news_add(request):

    if request.method == "POST":

        news_titel = request.POST.get('news_titel')
        news_short_txt = request.POST.get('news_short_txt')
        news_body_txt = request.POST.get('news_body_txt')
        new_news_item = News(news_titel=news_titel, news_short_txt=news_short_txt,
                             news_body_txt=news_body_txt, news_pic="-", news_url="-")
        new_news_item.save()
        return redirect('news_admin')
    return render(request, 'Back/news_add.html')


def news(request):

    news = News.objects.all().order_by('-pk')
    return render(request, 'Front/news.html', {'news': news})


def news_admin(request):

    news = News.objects.all()
    return render(request, 'Back/admin/news_list.html', {'news': news})
