from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/settings/add$', views.settings_add, name='settings_add'),
    url(r'^dashboard/settings/list$', views.settings_show, name='settings_show'),
]
