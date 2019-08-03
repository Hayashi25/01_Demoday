from django.urls import path, include
from website.views import index
from website.views import loja
from website.views import blog
from website.views import cadastro
from website.views import login
from website.views import aluno
from website.views import escola
from website.views import contato

urlpatterns = [
    path('', index),
    path('loja', loja),
    path('blog', blog),
    path('cadastro', cadastro),
    path('login', login),
    path('portaldoaluno', aluno),
    path('portaldaescola', escola),
    path('contato', contato)
]