from django.urls import path
from blog import views
urlpatterns=[
    path("index", views.ind, name='index'),
    path("day/",views.day, name ='day'),
]