from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')


# Создаем функцию для новой страницы
def new_page(request):
    return HttpResponse("<h2>Вторая страница моего проекта на Django.</h2>")