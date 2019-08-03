from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/slide/add$', views.slide_add, name='slide_add'),
]
