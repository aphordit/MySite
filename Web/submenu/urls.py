from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/submenu/add$', views.submenu_add, name='submenu_add'),
]
