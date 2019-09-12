from django.shortcuts import get_object_or_404, redirect, render
from .models import Settings


# Create your views here.

def settings_show(request):
    settings = Settings.objects.all()
    return render(request, 'Back/settings_list.html', {'settings': settings})


def settings_add(request):
    if not request.user.is_authenticated:   
        return redirect(privetlogin)
    if request.method == "POST":

        settings_name = request.POST.get('settings_name')
        settings_pic_url = request.POST.get('settings_pic_url')
        settings_head = request.POST.get('settings_head')
        settings_title = request.POST.get('settings_title')
        new_settings_item = Settings(settings_name=settings_name, settings_pic_url=settings_pic_url,
                                     settings_head=settings_head, settings_title=settings_title, settings_pic="")
        new_settings_item.save()
        return redirect('settings_show')
    return render(request, 'Back/admin/settings_add.html')


def settings_delete(request, pk):
    if not request.user.is_authenticated:   
        return redirect(privetlogin)
    delsettings = Settings.objects.filter(pk=pk)
    delsettings.delete()
    return redirect('settings_show')


def settings_item(request):

    item = Settings.objects.filter(settings_titel=wd)
    return render(request, 'Back/settings.html', {'settings': item})


def settings_edit(request, pk):
    if not request.user.is_authenticated:   
        return redirect(privetlogin)
    settingsedite = Settings.objects.filter(pk=pk)

    if request.method == "POST":

        settings_name = request.POST.get('settings_name')
        settings_pic_url = request.POST.get('settings_pic_url')
        settings_head = request.POST.get('settings_head')
        settings_title = request.POST.get('settings_title')

        b = Settings.objects.get(pk=pk)
        #b.settings_name = settings_name
        b.settings_pic_url = settings_pic_url
        b.settings_head = settings_head
        b.settings_title = settings_title
        b.save()
        return redirect('settings_show')
    return render(request, 'Back/settings_edit.html', {'settingsedite': settingsedite})
