from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import ArticleForm

def home(request):
    return render(request, 'home.html')

def blog(request):
    latest_articles = Article.objects.order_by('-data')[:10]
    return render(request, 'blog.html', {'latest_articles': latest_articles})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена!')
    
    return render(request, 'detail.html', {'article': a})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена!')

    a.comment_set.create(author_name = request.POST["comment_name"], comment_text = request.POST["comment_text"])

    return HttpResponseRedirect(reverse("article:detail", args=(a.id,)))

def create_theme(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog")

    form = ArticleForm()
    context = {
        "form": form
    }
    return render(request, 'create_theme.html', context)