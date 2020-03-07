from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('demo', views.demo, name = 'home-demo')
]