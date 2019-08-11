from django.db import models
from django.utils import timezone
from website.choices import REDES_ENSINO, TIPOS_ENSINO

# Create your models here.

class Escola(models.Model):

    nome_escola = models.CharField(
        max_length=255,
        verbose_name='Nome da Escola',
        unique=True,
        error_messages={'unique': 'Escola com este nome já está cadastrado em nosso sistema.'}
    )
    endereco_escola = models.CharField(
        max_length=255, 
        verbose_name='Endereço da Escola'
    )
    
    diretor_responsavel = models.CharField(
        max_length=12, 
        verbose_name='Diretor Responsável'
    )

    email = models.EmailField(
        max_length=255, 
        verbose_name='Email', 
        unique=True,
        error_messages={'unique': 'Este e-mail já está cadastrado em nosso sistema.'}
    )
    rede_ensino = models.CharField(
        max_length=255, 
        verbose_name='Rede de Ensino'
    )
    tipo_ensino = models.CharField(
        max_length=255, 
        verbose_name='Tipo de Ensino'
    )
    codigo_acesso = models.CharField(
        max_length=12, 
        verbose_name='Código de acesso', 
        unique=True,
        error_messages={'unique': 'Código de acesso já existente.'},
    )
    senha_acesso = models.CharField(
        max_length=12, 
        verbose_name='Senha de acesso',
    )

    confirmar_senha = models.CharField(
        max_length=12,
        verbose_name='Confirme a senha de acesso',
    )

    data_requisicao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_escola + ' - ' + self.rede_ensino


class Aluno(models.Model):

    TURMAS = (
        ('5 SERIE', '5 SERIE'),
        ('6 SERIE', '6 SERIE'),
        ('7 SERIE', '7 SERIE'),
        ('8 SERIE', '8 SERIE'),
        ('1 ANO', '1 ANO'),
        ('2 ANO', '2 ANO'),
        ('3 ANO', '3 ANO')
    )

    GENEROS = (
        ('Masculino', 'MASCULINO'),
        ('Feminino', 'FEMININO')
    )

    escola = models.ForeignKey(
        Escola, on_delete=models.CASCADE
    )

    nome_aluno = models.CharField(
        max_length=255,
        verbose_name='Nome do Aluno'
    )

    sobrenome_aluno = models.CharField(
        max_length=255,
        verbose_name='Sobrenome do Aluno'
    )

    nascimento_aluno = models.DateField(
        verbose_name='Data de Nascimento do Aluno'
    )

    idade_aluno = models.PositiveIntegerField(
        verbose_name='Idade do Aluno'
    )

    genero_aluno = models.CharField(
        max_length=255,
        verbose_name='Gênero do Aluno'
    )

    turma_aluno = models.CharField(
        max_length=255,
        verbose_name='Turma do Aluno',
        choices=TURMAS
    )

    pontuacao_aluno = models.PositiveIntegerField(
        verbose_name='Pontuação do Aluno',
        default=0
    )

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualização = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_aluno + ' ' + self.sobrenome_aluno


class Contato(models.Model):
    
    subject = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    
    from_email = models.EmailField(
        max_length=255,
        verbose_name='E-mail'
    )

    message = models.TextField(
        verbose_name='Mensagem'
    )

    data_mensagem = models.DateTimeField('Data',
    auto_now_add=True)

    def __str__(self):
        return self.subject + ' - ' + self.from_email