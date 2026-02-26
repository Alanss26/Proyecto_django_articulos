from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Article
from .forms import ArticleForm

class ArticleView(View):
    def get(self, request):
        return render(request, 'articles/articles_list.html')

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/articles_list.html'
    context_object_name = "articles_list"

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = "article"

class NewArticleForm(View):
    def get(self, request):
        form = ArticleForm()
        return render(request, 'articles/form_template.html', {'form': form})

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_articles')
        return render(request, 'articles/form_template.html', {'form': form})

class EditArticleView(View):
    def get(self, request, id):
        instance = get_object_or_404(Article, id=id)
        form = ArticleForm(instance=instance)
        return render(request, 'articles/form_template.html', {'form': form, 'object': instance})

    def post(self, request, id):
        instance = get_object_or_404(Article, id=id)
        form = ArticleForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('all_articles')
        return render(request, 'articles/form_template.html', {'form': form, 'object': instance})