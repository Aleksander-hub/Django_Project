from django.shortcuts import render
from news.models import Articles



def index(request):
    news = Articles.objects.order_by('-date')
    data = {
        'index': 'Главная страница',
        'news': news
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'about': 'Про нас'
    }
    return render(request, 'main/about.html', data)
    
def contacts(request):
    data = {
        'contacts': 'Контакты'
    }
    return render(request, 'main/contacts.html', data)

