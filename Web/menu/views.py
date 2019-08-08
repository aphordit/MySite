from django.shortcuts import get_object_or_404, redirect, render
from .models import Menu


# Create your views here.

def menu_add(request):
    if request.method == "POST":

        menu_name = request.POST.get('menu_name')
        menu_titel = request.POST.get('menu_titel')
        menu_link = request.POST.get('menu_link')
        new_menu_item = Menu(menu_name=menu_name, menu_titel=menu_titel,
                             menu_link=menu_link)
        new_menu_item.save()
        return redirect('menu_add')
    return render(request, 'Back/menu_add.html')
