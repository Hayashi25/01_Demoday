from django.shortcuts import render, redirect
from .forms import CadastroEscola, ContatarPessoas
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def loja(request):
    context = {}
    return render(request, 'loja.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def cadastro(request):
    if request.method == "POST":
        form = CadastroEscola(request.POST)
        if form.is_valid():
            escola = form.save()
            user = User.objects.create_user(username=request.POST['codigo_acesso'], password=request.POST['senha_acesso'],
                                            email=request.POST['email'])
            return redirect("/")
    else:
        form = CadastroEscola()
    
    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def aluno(request):
    context = {}
    return render(request, 'aluno.html', context)

def escola(request):
    context = {}
    return render(request, 'escola.html', context)

def contato(request):
    if request.method == "GET":
        form = ContatarPessoas()

    else:
        form = ContatarPessoas(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            pessoa = form.save()
            msg_email = str(from_email) + " - " + str(message)

            try: 
                send_mail(subject, msg_email, from_email, ['projeto.formiguinhaestacaohack@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/")

    context = {
        'form': form
    }

    return render(request, 'contato.html', context)