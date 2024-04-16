from django.urls import path

from . import views

urlpatterns = [
    path('a', views.indexs, name='index'),
    path('',views.index),

]