from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_page', views.new_page),
]
