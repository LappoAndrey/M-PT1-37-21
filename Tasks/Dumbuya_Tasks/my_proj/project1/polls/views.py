from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import LampType1, LampType2, LampType3, SelfDescription


def self(request):
    pics = SelfDescription.objects.all()
    return render(request, 'self.html', {'pics': pics})


def contact(request):
    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_email = request.POST["message-email"]
        message = request.POST['message']
        fake = 'fake'
        send_mail(
            message_name,
            'Email from' + ' ' + message_email + '\n' + message,
            fake,
            ['ayvari16@gmail.com']
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', )


def project_index(request):
    project1 = LampType1.objects.all()
    project2 = LampType2.objects.all()
    project3 = LampType3.objects.all()
    slice1 = LampType1.objects.all()[:1]
    slice2 = LampType2.objects.all()[:1]
    slice3 = LampType3.objects.all()[:1]
    context = {
        'project1': project1,
        'project2': project2,
        'project3': project3,
        'slice1': slice1,
        'slice2': slice2,
        'slice3': slice3,

    }
    return render(request, 'index.html', context)


def project_detail(request, pk):
    project = (LampType1.objects.get(pk=pk), LampType2.objects.get(pk=pk), LampType3.objects.get(pk=pk))

    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)


def lamp_page1(request):
    project1 = LampType1.objects.all()
    context = {
        'project1': project1

    }
    return render(request, 'lamptype1.html', context)


def lamp_page2(request):
    project2 = LampType2.objects.all()
    context = {
        'project2': project2

    }
    return render(request, 'lamptype2.html', context)


def lamp_page3(request):
    project3 = LampType3.objects.all()
    context = {
        'project3': project3

    }
    return render(request, 'lamptype3.html', context)
