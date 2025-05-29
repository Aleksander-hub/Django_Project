from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def news(request):
    all_articles = Articles.objects.order_by('-date')
    return render(request,'news/news.html', {'news': all_articles})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'
            
    form = ArticlesForm()
    data = {'form': form, 'error': error}
    return render(request,'news/create.html', data)
    