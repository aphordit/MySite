from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


def usermanager(request):

    return render(request, 'Back/usermanager.html')


def group_add(request):
    if request.method == "POST":
        name = request.POST.get('group')
        print(name)
        group = Group(name=name)
        group.save()
    return render(request, 'Back/grup_add.html')


def group_list(request):
    group = Group.objects.all()
    return render(request, 'Back/group_list.html', {'group': group})


def perm_add(request):

    if request.method == "POST":
        name = request.POST.get('perm_name')
        code = request.POST.get('perm_code')
        content = ContentType.objects.get(app_label='main', model='Main')
        print(name, code)
        perm = Permission.objects.create(
            name=name, codename=code, content_type=content)
        perm.save()
    return render(request, 'Back/perm_add.html')
