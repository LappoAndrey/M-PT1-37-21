from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from .models import Post, Author
from .forms import CommentForm, LoginForm, UserRegistrationForm, UserAuthorForm, AddPostModelForm
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required



# Create your views here.

def main_page(request):
    return render(request, 'untitled.html')


def post_list(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.filter(post=pk)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'article.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})



@permission_required('main.add_post')
def add_post(request):
    form = AddPostModelForm()

    if request.method == "POST":
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():
            post_entry = Post()
            post_entry.title = form.cleaned_data['title']
            post_entry.text = form.cleaned_data['text']
            post_entry.author = Author.objects.get(username=request.user.id)

            post_entry.save()

            return redirect('/')

    return render(request, 'new_post.html', {'form': form })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'untitled.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


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
        return render(request, 'registration.html', {'user_form': user_form})


def logoutUser(request):
    logout(request)
    return render(request, 'logged_out.html')


@login_required
def edit(request):
    if request.method == 'POST':
        profile_form = UserAuthorForm(data=request.POST)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = UserAuthorForm()
        return render(request,
                      'edit.html',
                      {'profile_form': profile_form})