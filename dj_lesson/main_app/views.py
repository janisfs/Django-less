from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Мой проект на Django.</h1>")


# Создаем функцию для новой страницы
def new_page(request):
    return HttpResponse("<h2>Вторая страница моего проекта на Django.</h2>")