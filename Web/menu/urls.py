from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/menu/add$', views.menu_add, name='menu_add'),
]
