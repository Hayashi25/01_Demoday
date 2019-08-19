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
        escola = Escola.objects.filter(email=request.user.email).first()
        print(request.user.email)
        print(escola)
        if form.is_valid():
            aluno = Aluno()
            aluno.nome_aluno = form.cleaned_data['nome_aluno']
            aluno.sobrenome_aluno = form.cleaned_data['sobrenome_aluno']
            aluno.nascimento_aluno = form.cleaned_data['nascimento_aluno']
            aluno.idade_aluno = form.cleaned_data['idade_aluno']
            aluno.genero_aluno = form.cleaned_data['genero_aluno']
            aluno.turma_aluno = form.cleaned_data['turma_aluno']
            aluno.pontuacao_aluno = form.cleaned_data['pontuacao_aluno']
            aluno.escola = escola
            aluno.save()
            messages.success(request, 'O aluno foi cadastrado.')
            return redirect ("/portaldaescola")
    else:
        form = CadastroAluno()
    
    context = {
        'form': form
        }
    return render(request, 'regaluno.html', context)

@login_required(login_url='/login')
def edicao_aluno(request, id):
    instance = get_object_or_404(Aluno, id=id)
    form = CadastroAluno(instance=instance)

    if request.method == 'POST':
        form = CadastroAluno(request.POST, instance=instance)

        if form.is_valid():
            instance.nome_aluno = form.cleaned_data['nome_aluno']
            instance.sobrenome_aluno = form.cleaned_data['sobrenome_aluno']
            instance.nascimento_aluno = form.cleaned_data['nascimento_aluno']
            instance.idade_aluno = form.cleaned_data['idade_aluno']
            instance.genero_aluno = form.cleaned_data['genero_aluno']
            instance.turma_aluno = form.cleaned_data['turma_aluno']
            instance.pontuacao_aluno = form.cleaned_data['pontuacao_aluno']
            instance.save()
            messages.success(request, 'O aluno foi editado.')
            return redirect ("/portaldaescola")

        elif(request.method == 'GET'):
            return render(request, 'editaluno.html', {'form':form, 'instance':instance})

        else:
            return render(request, 'editaluno.html', {'form':form, 'instance':instance})

    return render(request, 'editaluno.html', {'form': form}, {'instance': instance})

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