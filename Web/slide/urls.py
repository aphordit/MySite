from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^slide/add$', views.news_add, name='slide_add'),
]
