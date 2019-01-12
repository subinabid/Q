from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('<int:que_id>/', views.que, name='que'),
    path('<int:que_id>/submit', views.submit, name='submit'),
    path('submission', views.submission, name='submission')
]
