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
        content = ContentType.objects.get(app_label='main', model='main')
        print(name, code)
        perm = Permission.objects.create(
            name=name, codename=code, content_type=content)
        perm.save()
    return render(request, 'Back/perm_add.html')


def perm_to_gr(request):
    if request.method == "POST":
        gr_name = request.POST.get('gr_name')
        perm_name = request.POST.get('perm_name')
        group = Group.objects.get(name=gr_name)
        perm = Permission.objects.get(name=perm_name)
        #print("gr = " + group + "pr = " + perm)
        group.permissions.add(perm)
    return render(request, 'Back/perm_to_gr.html')


def user_to_gr(request):
    if request.method == "POST":
        gr_name = request.POST.get('gr_name')
        user_name = request.POST.get('user_name')
        group = Group.objects.get(name=gr_name)
        user = User.objects.get(username=user_name)
        #print("gr = " + group + "pr = " + perm)
        print(group, user)
        user.groups.add(group)
    return render(request, 'Back/user_to_gr.html')
