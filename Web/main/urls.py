from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^login/$', views.privetlogin, name='privetlogin'),
    url(r'^register/$', views.admin_register, name='admin_register'),
    url(r'^logout/$', views.admin_logout, name='admin_logout'),
]
