from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excluir/', views.excluir, name='excluir'),
    path('pdf/', views.html_to_pdf_view, name='html_to_pdf_view'),
]