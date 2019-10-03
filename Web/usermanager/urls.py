from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/usermanager$', views.usermanager, name='usermanager'),
    url(r'^dashboard/group/add$', views.group_add, name='group_add'),
    url(r'^dashboard/group/list$', views.group_list, name='group_list'),
    url(r'^dashboard/permission/add$', views.perm_add, name='perm_add'),
]
