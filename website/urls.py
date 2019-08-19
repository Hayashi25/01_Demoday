from django.urls import path, include
from website.views import index
from website.views import loja
from website.views import blog
from website.views import cadastro_escola
from website.views import edicao_aluno
from website.views import page_edicao
from website.views import login_escola
from website.views import logout_user
from website.views import escola
from website.views import cadastro_aluno
from website.views import contato

urlpatterns = [
    path('', index),
    path('loja', loja),
    path('blog', blog),
    path('cadastro', cadastro_escola),
    path('login', login_escola),
    path('logout', logout_user),
    path('portaldaescola', escola),
    path('registrodealuno', cadastro_aluno),
    path('edicaodealuno', page_edicao),
    path('edicaoaluno/<int:id>', edicao_aluno),
    path('contato', contato)
]