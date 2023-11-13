from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creditos/', views.credito, name='credito')
]