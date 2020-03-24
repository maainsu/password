from django.urls import path
from account import views
urlpatterns=[
    path('basic/', views.post_index, name='post_index'),
    path('signup/', views.post_sign_up, name='sign_up'),
    path('', views.index, name ='index'),
    path('login/', views.login1, name='login'),
    path('comp/', views.comp, name = 'comp'),
]