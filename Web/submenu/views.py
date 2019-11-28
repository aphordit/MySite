from django.shortcuts import get_object_or_404, redirect, render
from menu.models import Menu
from .models import Submenu
# Create your views here.


def submenu_add(request):
    if not request.user.is_authenticated:
        return redirect(privetlogin)

    menu = Menu.objects.all()

    if request.method == "POST":
        sub_name = request.POST.get('sub_name')
        menu_id = request.POST.get('menu_id')
        menu_name = Menu.objects.get(pk=menu_id).menu_name
        print(sub_name, menu_name, menu_id)
        new_submenu = Submenu(
            sub_name=sub_name, menu_name=menu_name, menu_id=menu_id)
        new_submenu.save()
        return redirect('submenu_add')
    return render(request, 'Back/submenu_add.html', {'menu': menu})
