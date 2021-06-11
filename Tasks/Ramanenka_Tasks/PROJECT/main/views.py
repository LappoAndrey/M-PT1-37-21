from django.http.response import HttpResponseNotFound, HttpResponse, HttpResponseBadRequest
from django.urls.base import reverse, reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group



def news(request):
    all_news = Nnews.objects.all()
    return render(request, 'main/news.html', {'news': all_news})


def nnews(request, nnews_id):
    try:
        n = Nnews.objects.get(id=nnews_id)
    except:
        return HttpResponseNotFound('Sorry, this page doesn\'t exist')
    return render(request, 'main/nnews.html', {'nnews': n})


def about(request):
    return render(request, 'main/about.html')


def sign_in(request):
    return render(request, 'main/login.html')


def log_out(request):
    logout(request)
    return render(request, 'main/log_out.html')


def test0(request):
    return render(request, 'main/test0.html')



# @login_required(login_url=reverse_lazy("login"))
def profile(request):
    result = Result.objects.filter(user=request.user)
    return render(request, 'registration/profile.html', context={"results": result})
    # return render(request, 'registration/profile.html')
    

def register(request):
        if request.method == 'POST':
            form = SigUpForm(request.POST)
            if form.is_valid():
                form.save()
                user_instance: User = form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                typeuser = form.cleaned_data.get('status')
                group = None
                if typeuser in ('Students', 'Professors'):
                    group = Group.objects.filter(name=typeuser).first()
                    print(group)
                    print(typeuser)
                if not group:
                    return HttpResponseBadRequest()
                user_instance.groups.add(group)
                user = authenticate(request, username=username, password=raw_password)
                login(request, user)
                return redirect('profile')
        else:
            form = SigUpForm()
        return render(request, 'registration/register.html', {'form': form})


def results(request):
    result = Result.objects.filter(user=request.user)
    # print(result)
    return render(request, 'main/results.html', {'results': result})


def index(request):
    questions = Choice.objects.all().order_by('-id')
    if request.method == 'GET':
        return render(request, 'main/index.html', {'questions': questions})
    elif request.method == "POST":
        answers = {int(key.split("_")[1]): int(value) for key, value in request.POST.items() if key.startswith("key")}
        right_answers = {index: question.key for index, question in enumerate(questions)}
        if len(answers) != len(right_answers):
            return render(request, 'main/index.html', {'questions': questions, "notification": "Answer all questions please"})
        for question, a in right_answers.items():
            Result.objects.create(user=request.user, question=questions[question], result=answers[question] == a)
        # print(results)
        # return render(request, 'main/results.html')
    return redirect( 'results')
        # return HttpResponse()


@permission_required('main.add_choice' )
def create(request):
    error = ''
    if request.method == "POST":
        form = AddquestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not correct'
    form = AddquestionsForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create.html', context)


def edit(request, id):
    try:
        questions = Choice.objects.get(id=id)
        if request.method == "POST":
            form = AddquestionsForm(request.POST)
            form.save()
            return redirect('home')
        else:
            error = 'Form is not correct'
        form = AddquestionsForm()
    except Choice.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")
    

    # try:
    #     person = Person.objects.get(id=id)
 
    #     if request.method == "POST":
    #         person.name = request.POST.get("name")
    #         person.age = request.POST.get("age")
    #         person.save()
    #         return HttpResponseRedirect("/")
    #     else:
    #         return render(request, "edit.html", {"person": person})
    # except Person.DoesNotExist:
    #     return HttpResponseNotFound("<h2>Person not found</h2>")
     

# def delete(request, id):
#     try:
#         questions = Choice.objects.get(id=id)
#         choice.delete()
#         return HttpResponseRedirect("")
#     except Choice.DoesNotExist:
#         return HttpResponseNotFound("<h2>Question not found</h2>")



