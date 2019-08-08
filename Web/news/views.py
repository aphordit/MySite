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


def news_delete(request, pk):

    delnews = News.objects.filter(pk=pk)
    delnews.delete()
    return redirect('news_admin')


def news_show(request, wd):

    shownews = News.objects.filter(news_titel=wd)
    return render(request, 'Front/shownews.html', {'news': shownews})


def news_edit(request, pk):
    newsedite = News.objects.filter(pk=pk)

    if request.method == "POST":

        news_titel = request.POST.get('news_titel')
        news_short_txt = request.POST.get('news_short_txt')
        news_body_txt = request.POST.get('news_body_txt')

        b = News.objects.get(pk=pk)
        #b.news_titel = news_titel
        b.news_short_txt = news_short_txt
        b.news_body_txt = news_body_txt
        b.save()
        return redirect('news_admin')
    return render(request, 'Back/news_edit.html', {'newsedite': newsedite})
