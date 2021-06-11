from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from pip._internal import req


from .models import *
from django.contrib.auth.decorators import permission_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token

from .models import MAIN
from .models import USERS





@requires_csrf_token
def index(request):
    name = request.GET.get('name', '')
    message = request.GET.get('messages', '')
    email = request.GET.get('mail', '')
    tema = request.GET.get('tema', '')

    if name and message and email and tema:
        try:
            send_mail('Новое сообщение!',
            'Тема вопроса: '+str(tema)+'. '+' Сообщение: '+str(message)+'. '+'От: '+str(name)+' '+str(email), 'mounted.rk@gmail.com', ['bingo.bax@mail.ru'])
            return render(request, 'index.html')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    return render(request, 'index.html')




def home(request):
    return render(request, 'account/home.html')


def authorization(request):
    user = USERS()
    modelmain = MAIN.objects.all()[900:1050]
    if request.method == "POST":
        login = request.POST.get('login')
        password = request.POST.get('password')
        if USERS.objects.filter(login=login, password=password).exists():
            return render(request, 'small_wholesale.html',{'login':login,'password':password, "modelmain":modelmain})
        else:
            message=1
            return render(request, 'account/authorization.html',{'message':message})
    return render(request, 'account/authorization.html', {"modelmain":modelmain})





def registration(request):
    model_firms=FIRMS.objects.all()
    user = USERS()
    message=''
    if request.method == "POST":
        login = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        firma = request.POST.get('firma_id')
        password2 = request.POST.get('password2')
        if len(password)>10:
            if password2==password:
                user.login=login
                user.password=password
                user.email=email
                user.idfirm=FIRMS.objects.get(id=firma)
                user.mac='NULL'
                user.dtCameLats=datetime.now()
                user.dtCheck=datetime.now()
                user.date_from=datetime.now()
                user.date_to=datetime.now()
                user.ipCame='NULL'
                user.ipCheck = 'NULL'
                user.srcfile = 'NULL'
                user.typebd=0

                user.save()
                message = 2
                return render(request, 'account/authorization.html',{'message':message})
            else:
                message=0
                return render(request, 'account/registration.html', {"model_firms": model_firms,"message":message})
        else:
            message = 1
            return render(request, 'account/registration.html', {"model_firms": model_firms, "message": message})


    return render(request, 'account/registration.html',{"model_firms":model_firms})




@permission_required('app.small_wholesale')
def small_wholesale(request):

    modelmain = MAIN.objects.all()[900:1050]

    return render(request, 'small_wholesale.html',{"modelmain":modelmain})






















# def posts(request, query='reverse'):
#     all_posts = Post.objects.all()

#     print(query)

#     if query == 'reverse':
#         all_posts = all_posts[::-1]

#     result = '<h1>All Posts:</h1><ul>'

#     viewed_posts = request.session.get('viewed_posts', {})
#     print(viewed_posts)

#     return render(request, 'posts.html', {'posts': all_posts, 'viewed_posts': viewed_posts})




# def home(request):
#     print("hello")
#     return render(request, 'home.html')




# def posts(request, query='reverse'):
#     all_posts = Post.objects.all()

#     print(query)

#     if query == 'reverse':
#         all_posts = all_posts[::-1]

#     result = '<h1>All Posts:</h1><ul>'

#     viewed_posts = request.session.get('viewed_posts', {})
#     print(viewed_posts)

#     return render(request, 'posts.html', {'posts': all_posts, 'viewed_posts': viewed_posts})






# def post(request, post_id):
#     try:
#         p = Post.objects.get(id=post_id)
#     except:
#         return HttpResponseNotFound('Ooooops')
    
#     print(type(p.id))

#     viewed_posts = request.session.get('viewed_posts', {})
#     viewed_posts[post_id] = post_id
#     request.session['viewed_posts'] = viewed_posts
#     return render(request, 'post.html', {'post': p})

# @permission_required('app.add_post')
# def add_post(request):

#     form = AddPost()

#     if request.method == "POST":
#         form = AddPost(request.POST, request.FILES)

#         if form.is_valid():

#             post_entry = Post()
#             post_entry.title = form.cleaned_data['title']
#             post_entry.subtitle = form.cleaned_data['subtitle']
#             post_entry.content = form.cleaned_data['content']
#             post_entry.post_type = form.cleaned_data['post_type']
#             post_entry.image = form.cleaned_data['image']

#             post_entry.issued = datetime.datetime.now()
#             post_entry.author = Author.objects.get(username=request.user.username)

#             post_entry.save()

#             return redirect('posts')

#     return render(request, 'add_post.html', {'form': form})
