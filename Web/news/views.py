from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage
import datetime
from datetime import date
from django.utils import timezone
from main.dateconverter import shamsiDate
from .models import News
from django.contrib.auth.models import User
from usermanager.models import Usermanager
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from menu.models import Menu
from submenu.models import Submenu
import random

# Create your views here.


def news_add(request):

    print('11111111111111111111111111111')

    if request.user.has_perm('news.news_add'):
        print('okokokokokokokkokoko')

    submenu = Submenu.objects.all()

    now = datetime.datetime.now()
    year = str(now.year)
    month = now.month
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)
    day = now.day
    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)
    today = shamsiDate(int(year), int(month), int(day))
    print(today)
    if request.method == "POST":

        news_titel = request.POST.get('news_titel')
        news_short_txt = request.POST.get('news_short_txt')
        news_body_txt = request.POST.get('news_body_txt')
        submenu_id = request.POST.get('menu_id')
        rand = str(random.randint(1000, 9999))
        tt = today.replace('/', "")
        rand = tt + rand
        while len(News.objects.filter(rand=rand)) != 0:
            rand = random.rand(1000, 9999)
            rand = tt + rand
        print(rand)
        try:
            if str(request.FILES['MyFile'].content_type).startswith("image"):
                MyFile = request.FILES['MyFile']
                fs = FileSystemStorage()
                filename = fs.save(MyFile.name, MyFile)
                url = fs.url(filename)
                menu_id = Submenu.objects.get(pk=submenu_id).menu_id
                new_news_item = News(news_titel=news_titel, news_short_txt=news_short_txt,
                                     news_body_txt=news_body_txt, news_pic=filename, news_url=url, date=today, menu_id=menu_id, submenu_id=submenu_id, rand=rand)
                new_news_item.save()
                return redirect('news_admin')
            else:
                print("salam")
        except:
            print("Not Valid Upload")

    return render(request, 'Back/news_add.html', {'submenu': submenu})


def news(request):

    news = News.objects.all().order_by('-pk')

    paginator = Paginator(news, 1)
    page = request.GET.get('page')
    try:
        newss = paginator.page(page)
    except PageNotAnInteger:
        newss = paginator.page(1)
    except EmptyPage:
        newss = paginator.page(paginator.num_page)

    b = round(len(news)/1)

    lis = list(range(b))

    return render(request, 'Front/news.html', {'newss': newss, 'lis': lis})


def news_admin(request):
    if not request.user.is_authenticated:
        return redirect('privetlogin')
    news = News.objects.all()
    return render(request, 'Back/admin/news_list.html', {'news': news})


def news_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('privetlogin')
    print(user.has_perm('news_delete'))
    print(user.has_perm())
    delnews = News.objects.filter(pk=pk)
    fs = FileSystemStorage()
    picname = News.objects.get(pk=pk).news_pic
    fs.delete(picname)
    delnews.delete()
    return redirect('news_admin')


def news_show(request, wd):

    shownews = News.objects.filter(news_titel=wd)
    return render(request, 'Front/shownews.html', {'news': shownews})


def news_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('privetlogin')
    newsedite = News.objects.filter(pk=pk)
    if request.method == "POST":

        news_titel = request.POST.get('news_titel')
        news_short_txt = request.POST.get('news_short_txt')
        news_body_txt = request.POST.get('news_body_txt')

        try:

            news = News.objects.get(pk=pk)
            MyFile = request.FILES['MyFile']
            fs = FileSystemStorage()
            fs.delete(news.news_pic)
            filename = fs.save(MyFile.name, MyFile)
            url = fs.url(filename)

            b = News.objects.get(pk=pk)
            b.news_titel = news_titel
            b.news_short_txt = news_short_txt
            b.news_body_txt = news_body_txt
            b.news_pic = filename
            b.news_url = url
            b.save()

        except:

            b = News.objects.get(pk=pk)
            b.news_titel = news_titel
            b.news_short_txt = news_short_txt
            b.news_body_txt = news_body_txt
            b.save()

        return redirect('news_admin')
    return render(request, 'Back/news_edit.html', {'newsedite': newsedite})
