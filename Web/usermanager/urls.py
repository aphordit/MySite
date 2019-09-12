from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/usermanager$', views.usermanager, name='usermanager'),
]
