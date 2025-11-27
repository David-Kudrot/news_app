from django.shortcuts import render, get_object_or_404
from .models import Article
from django.utils import timezone




def index(request):
    articles = Article.objects.all()
    ticker_items = Article.objects.filter(is_latest=True)[:10]
    if not ticker_items.exists():
        ticker_items = Article.objects.all()[:10]
    return render(request, 'index.html', {
        'articles': articles,
        'ticker_items': ticker_items,
        'current_year': timezone.now().year,
    })




def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', {'article': article})