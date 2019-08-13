from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/settings/add$', views.settings_add, name='settings_add'),
]
