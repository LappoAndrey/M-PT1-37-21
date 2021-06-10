from django.shortcuts import render, redirect
from django.views.generic.dates import DateMixin
from .models import Article, Author
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from .forms import AddArticle
import datetime
from .forms import UserRegistrationForm



def home(request):
    return render(request, 'home.html')


def blog(request):

    latest_articles = Article.objects.order_by('-data')[:10]

    viewed_articles = {int(k): v for k, v in request.session.get('viewed_articles', {}).items()} 
    
    return render(request, 'blog.html', {'latest_articles': latest_articles, "viewed_articles": viewed_articles})


def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('There is no article!')
    
    latest_comments = a.comment_set.order_by("-id")[:10]

    viewed_articles = request.session.get('viewed_articles', {})
    viewed_articles.setdefault(str(article_id), 0)
    viewed_articles[str(article_id)] += 1
    request.session['viewed_articles'] = viewed_articles

    return render(request, 'detail.html', {'article': a, "latest_comments": latest_comments})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('There is no article!')

    a.comment_set.create(author_name = request.POST["comment_name"], comment_text = request.POST["comment_text"])

    return HttpResponseRedirect(reverse("detail", args=(a.id,)))


@permission_required('app.add_article')
def add_article(request):
    
    form = AddArticle()

    if request.method == "POST":
        form = AddArticle(request.POST, request.FILES)

        if form.is_valid():
            post_entry = Article()
            post_entry.title = form.cleaned_data["title"]
            post_entry.content = form.cleaned_data["content"]
            post_entry.image = form.cleaned_data["image"]

            post_entry.data = datetime.datetime.now()
            post_entry.author = Author.objects.get(username=request.user.username)

            post_entry.save()

            return redirect("blog")
    return render(request, "add_article.html", {"form": form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})