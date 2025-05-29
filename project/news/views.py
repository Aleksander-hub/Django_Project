from django.shortcuts import render
from .models import Articles

def news(request):
    all_articles = Articles.objects.order_by('-date')
    return render(request,'news/news.html', {'news': all_articles})

def create(request):
    return render(request,'news/create.html')