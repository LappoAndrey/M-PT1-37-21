from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Post
from django.contrib.auth.decorators import permission_required
from .forms import AddPostModelForm
import datetime
from rest_framework import viewsets
from .serializers import PostSerializer

def home(request):
    print("hello")
    return render(request, 'home.html')

def posts(request, query='reverse'):
    all_posts = Post.objects.all()

    print(query)

    if query == 'reverse':
        all_posts = all_posts[::-1]

    result = '<h1>All Posts:</h1><ul>'

    viewed_posts = request.session.get('viewed_posts', {})
    print(viewed_posts)

    return render(request, 'posts.html', {'posts': all_posts, 'viewed_posts': viewed_posts})

def post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        return HttpResponseNotFound('Ooooops')
    
    print(type(p.id))

    viewed_posts = request.session.get('viewed_posts', {})
    viewed_posts[post_id] = post_id
    request.session['viewed_posts'] = viewed_posts
    return render(request, 'post.html', {'post': p})

@permission_required('app.add_post')
def add_post(request):

    form = AddPostModelForm()

    if request.method == "POST":
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():

            post_entry = Post()
            post_entry.title = form.cleaned_data['title']
            post_entry.subtitle = form.cleaned_data['subtitle']
            post_entry.content = form.cleaned_data['content']
            post_entry.post_type = form.cleaned_data['post_type']
            post_entry.image = form.cleaned_data['image']

            post_entry.issued = datetime.datetime.now()
            post_entry.author = Author.objects.get(username=request.user.username)

            post_entry.save()

            return redirect('posts')

    return render(request, 'add_post.html', {'form': form})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer