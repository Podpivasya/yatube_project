from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):    
    return HttpResponse('Главная страница ы')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse('Список групп ы')
