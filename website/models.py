from django.db import models,

# Create your models here.

class Escola(models.Model):

    REDES_ENSINO = (
        ('Estadual', 'Estadual'),
        ('Municipal', 'Municipal'),
        ('Federal', 'Federal'),
        ('Particular', 'Particular'),
        ('Outra', 'Outra')
    )

    TIPOS_ENSINO = (
        ('Ensino Fundamental', 'Ensino Fundamental'),
        ('Ensino Médio', 'Ensino Médio'),
        ('Ambos', 'Ambos')
    )

    nome_escola = models.CharField(
        max_length=255,
        verbose_name='Nome da Escola'
    )

    endereco_escola = models.CharField(
        max_length=255,
        verbose_name='Endereço da Escola'
    )

    telefone_escola = models.PositiveIntegerField(
        max_length=10,
        verbose_name='Telefone da Escola'
    )

    email_escola = models.EmailField(
        max_length=255,
        verbose_name='E-mail da Escola'
        unique=True
    )

    rede_ensino = models.CharField(
        max_length=255,
        verbose_name='Rede de Ensino da Escola',
        choices=REDES_ENSINO
    )

    tipo_ensino = models.CharField(
        max_length=255,
        verbose_name='Tipo de Ensino da Escola',
        choices=TIPOS_ENSINO
    )

    codigo_acesso = models.CharField(
        max_length=255,
        verbose_name='Código de acesso',
        unique=True
    )

    senha_acesso = models.CharField(
        max_length=255,
        verbose_name='Senha de acesso',
        unique=True
    )

    data_requisicao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_escola + ' ' + self.rede_ensino