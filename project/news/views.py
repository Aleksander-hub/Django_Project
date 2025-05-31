from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView



def news(request):
    all_articles = Articles.objects.order_by('-date')
    return render(request,'news/news.html', {'news': all_articles})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm
    success_url = '/news/'

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'



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

def news_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    return render(request, 'news/news_detail.html', {'article': article})
    