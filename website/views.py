from django.shortcuts import render

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
    context = {}
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
    context = {}
    return render(request, 'contato.html', context)