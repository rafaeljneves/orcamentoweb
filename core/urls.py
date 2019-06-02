from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excluir', views.excluir, name='excluir'),
]