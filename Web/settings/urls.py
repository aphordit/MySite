from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/settings/add$', views.settings_add, name='settings_add'),
    url(r'^dashboard/settings/list$', views.settings_show, name='settings_show'),
    url(r'^dashboard/settings/delete/(?P<pk>\d+)/$',
        views.settings_delete, name='settings_delete'),
    url(r'^dashboard/settings/edit/(?P<pk>\d+)/$',
        views.settings_edit, name='settings_edit'),
]
