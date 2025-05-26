from django.shortcuts import render



def index(request):
    data = {
        'index': 'Главная страница'
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

