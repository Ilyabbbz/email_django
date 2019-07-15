from django.shortcuts import render, redirect
from django.core.mail import send_mail
from config import EMAIL_USER


def index(request):

    context = {}

    return render(request, 'index.html', context=context)


def email(request):

    subject = request.POST['subject']
    message = request.POST['message']
    email_from = EMAIL_USER
    recipient_list = ['ilyabbbz@gmail.com', ]

    send_mail(subject, message, email_from, recipient_list)

    print(request.POST)
    return redirect('index')
