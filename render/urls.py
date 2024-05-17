from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/handle',views.handle_button, name='handle_button'),

]