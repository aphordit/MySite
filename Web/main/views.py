from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Main
from news.models import News
from slide.models import Slide
from settings.models import Settings
from usermanager.models import Usermanager
from django.conf import settings
from django.core.mail import send_mail
from menu.models import Menu
from submenu.models import Submenu
import random
import string
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
# Create your views here.


def home(request):
    news = News.objects.all().order_by('-pk')[:3]
    slides = Slide.objects.all()
    settings = Settings.objects.all()

    subject = 'KarafarinShow'
    message = 'txt'
    # email_from = settings.email_user
    # recipient_list = ['bahreinifoad@gmail.com', ]
    # send_mail(subject, message, email_from, recipient_list)

    return render(request, 'Front/home.html', {'news': news, 'slides': slides, 'settings': settings})


def home2(request):
    menu = Menu.objects.all()
    submenu = Submenu.objects.all()
    rand = ''
    for i in range(100):
        rand = rand + random.choice(string.ascii_letters)
    count = News.objects.count()
    randnewsname = News.objects.all()[random.randint(0, count-1)]
    rand = random.randint(1000000000, 9999999999)
    fill = News.objects.filter(date__gte='1398/01/02', date__lte='1398/07/02')
    tilname = News.objects.filter(news_titel__contains='شی')
    ip, is_routable = get_client_ip(request)
    country = "-"
    try:
        response = DbIpCity.get('5.190.112.0', api_key='free')
        country = response.country + "|" + response.city
    except:
        print('not ssssssssssssssssssssssssssssssssssssssssssssss')
    return render(request, 'Front/home2.html', {'menu': menu, 'submenu': submenu, 'rand': rand, 'randnewsname': randnewsname, 'fill': fill, 'tilname': tilname, 'ip': ip, 'is_routable': is_routable, 'country': country})


def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('privetlogin')
    if Usermanager.objects.get(uname=request.user).level != '1001':
        return render(request, 'Back/user/Dashboard.html')

    print(request.user)

    print(request.user.groups.all())

    for g in request.user.groups.all():
        print("groupname=")
        print(g.name)
    return render(request, 'Back/admin/Dashboard.html')


def privetlogin(request):

    logout(request)

    if request.method == "POST":
        admin_username = request.POST.get('admin_username')
        admin_pass = request.POST.get('admin_pass')
        print(admin_username, admin_pass)
        admin_auth = authenticate(username=admin_username, password=admin_pass)

        print(admin_auth)
        if admin_auth != None:
            login(request, admin_auth)
            print("okokokokokokk")
            return redirect('dashboard')
            print(admin_username, admin_pass)
    return render(request, 'Back/admin/login.html')


def admin_register(request):
    if request.method == "POST":
        admin_username = request.POST.get('admin_username')
        email = request.POST.get('email')
        admin_pass = request.POST.get('admin_pass')
        admin_pass2 = request.POST.get('admin_pass2')
        print(admin_username, admin_pass, email)
        if admin_pass == admin_pass2:
            user = User.objects.create_user(
                username=admin_username, email=email, password=admin_pass)
            login(request, user)
            b = Usermanager(uname=admin_username, email=email,
                            level="1002", group='admin_level_1')
            b.save()

            return redirect('dashboard')

    return render(request, 'Back/admin/register.html')


def admin_logout(request):
    logout(request)
    return redirect('privetlogin')
