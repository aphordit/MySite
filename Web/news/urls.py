from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/news/add$', views.news_add, name='news_add'),
    url(r'^news/$', views.news, name='news'),
    url(r'^dashboard/news/list$', views.news_admin, name='news_admin'),
]
