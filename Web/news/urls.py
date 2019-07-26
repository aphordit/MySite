from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^news/add$' , views.news_add, name='news_add') ,
]

