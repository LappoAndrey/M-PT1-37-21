from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .forms import AddPost
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(ListView):
    model = Article
    paginate_by = 3
    template_name = 'news.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'


class ArticleLastView(ListView):
    model = Article
    paginate_by = 3
    template_name = 'lastnews.html'


@method_decorator(permission_required('news.add_article'), name='dispatch')
class NewsManager(LoginRequiredMixin, CreateView):
    form_class = AddPost
    template_name = 'adminpanel.html'
    success_url = '/news/'

    def form_valid(self, form_class):
        form_class.instance.author = self.request.user
        return super().form_valid(form_class)
