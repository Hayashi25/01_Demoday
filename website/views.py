from .forms import CadastroEscola, CadastroAluno, ContatarPessoas
from .models import Escola, Aluno, Contato
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    context = {}
    return render(request, 'index.html', context)

def loja(request):
    context = {}
    return render(request, 'loja.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def cadastro_escola(request):
    if request.method == "POST":
        form = CadastroEscola(request.POST)
        if form.is_valid():
            escola = form.save()
            user = User.objects.create_user(username=request.POST['codigo_acesso'],
                                            password=request.POST['senha_acesso'],
                                            email=request.POST['email'])
            return render(request, 'login.html')
    else:
        form = CadastroEscola()
    
    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context)

def login_escola(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect ("/portaldaescola")
        else:
            messages.error(request, 'Usuário e/ou senha inválido(s). Favor tentar novamente.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def escola(request):
    context = {}
    return render(request, 'escola.html', context)

@login_required(login_url='/login')
def cadastro_aluno(request):
    if request.method == "POST":
        form = CadastroAluno(request.POST)
        if form.is_valid():
            aluno = form.save()
            return redirect ("/portaldaescola")
    else:
        form = CadastroAluno()
    
    context = {
        'form': form
        }
    return render(request, 'regaluno.html', context)

# def editar_aluno(request, id):
#     post = get_object_or_404(Post, pk=id)
#     form = PostForm (instance=post)

#     if(request=)


def contato(request):
    if request.method == "GET":
        form = ContatarPessoas()

    else:
        form = ContatarPessoas(request.POST)
        if form.is_valid():
            pessoa = form.save()
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
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