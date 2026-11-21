from datetime import date          # para comparar datas de vencimento
from decimal import Decimal        # tipo numérico exato para dinheiro (evita erros de float)

from django.contrib.auth.models import User   # usuário nativo do Django (o mesmo do login)
from django.db import models


# ---------------------------------------------------------------
# Categoria  ->  tabela tb_categoria
# Cadastrada pela equipe via Django Admin (ex.: Streaming, Estudos).
# ---------------------------------------------------------------
class Categoria(models.Model):
    # Chave primária com o nome do nosso modelo lógico (em vez do 'id' padrão)
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    # null=True -> aceita NULL no banco | blank=True -> pode ficar vazio no formulário
    descricao = models.CharField(max_length=200, null=True, blank=True)
    cor_identificacao = models.CharField(max_length=7, null=True, blank=True)  # ex.: #6C5CE7

    class Meta:
        db_table = 'tb_categoria'      # nome da tabela no banco
        ordering = ['nome']            # ordem padrão das consultas
        verbose_name = 'Categoria'     # como aparece no admin
        verbose_name_plural = 'Categorias'

    def __str__(self):
        # Texto que representa o objeto (admin, listas, selects)
        return self.nome


# ---------------------------------------------------------------
# Assinatura  ->  tabela tb_assinatura
# ---------------------------------------------------------------
class Assinatura(models.Model):
    # Opções fixas (choices): (valor gravado no banco, texto mostrado ao usuário)
    MOEDAS = [
        ('BRL', 'Real (BRL)'),
        ('USD', 'Dólar (USD)'),
        ('EUR', 'Euro (EUR)'),
    ]
    CICLOS = [
        ('MENSAL', 'Mensal'),
        ('ANUAL', 'Anual'),
    ]

    id_assinatura = models.AutoField(primary_key=True)

    # ForeignKey = relação 1:N. Um usuário tem várias assinaturas.
    # on_delete=CASCADE -> apagar o usuário apaga as assinaturas dele.
    # db_column         -> nome da coluna no banco (igual ao modelo lógico).
    # related_name      -> permite usuario.assinaturas.all() no sentido inverso.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,
                                db_column='id_usuario', related_name='assinaturas')

    # PROTECT -> o Django impede apagar uma categoria que ainda tem assinaturas.
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT,
                                  db_column='id_categoria', related_name='assinaturas')

    nome_servico = models.CharField(max_length=100)
    # DecimalField: até 10 dígitos no total, 2 depois da vírgula (bom para dinheiro)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    moeda = models.CharField(max_length=3, choices=MOEDAS, default='BRL')
    ciclo_cobranca = models.CharField(max_length=10, choices=CICLOS, default='MENSAL')
    data_vencimento = models.DateField()
    eh_free_trial = models.BooleanField(default=False)
    data_limite_trial = models.DateField(null=True, blank=True)  # só vale se for free trial

    class Meta:
        db_table = 'tb_assinatura'
        ordering = ['data_vencimento']   # as que vencem primeiro aparecem primeiro
        verbose_name = 'Assinatura'
        verbose_name_plural = 'Assinaturas'

    def __str__(self):
        return f"{self.nome_servico} - {self.valor} {self.moeda}"

        # Quantos dias faltam para o vencimento (negativo = já venceu)
    def dias_para_vencer(self):
        # subtrair duas datas devolve um timedelta; .days é a diferença em dias
        return (self.data_vencimento - date.today()).days

    # Método do nosso diagrama de classes: estaProximaDoVencimento(dias)
    def esta_proxima_do_vencimento(self, dias=7):
        # True se vence hoje ou nos próximos 'dias' (nunca se já venceu)
        return 0 <= self.dias_para_vencer() <= dias

    # True se a data de vencimento já passou
    def esta_vencida(self):
        return self.dias_para_vencer() < 0

    # Método do nosso diagrama de classes: calcularValorEmBRL(cotacao)
    def calcular_valor_em_brl(self, cotacao):
        if self.moeda == 'BRL':
            return self.valor   # já está em reais, não converte
        # valor x cotação, arredondado em 2 casas
        return (self.valor * cotacao).quantize(Decimal('0.01'))


# ---------------------------------------------------------------
# PessoaVinculada  ->  tabela tb_pessoa_vinculada
# Contatos que o usuário cadastra para dividir assinaturas.
# ---------------------------------------------------------------
class PessoaVinculada(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    usuario_dono = models.ForeignKey(User, on_delete=models.CASCADE,
                                     db_column='id_usuario_dono', related_name='pessoas_vinculadas')
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'tb_pessoa_vinculada'
        ordering = ['nome']
        verbose_name = 'Pessoa vinculada'
        verbose_name_plural = 'Pessoas vinculadas'

    def __str__(self):
        return self.nome


# ---------------------------------------------------------------
# DivisaoAssinatura  ->  tabela tb_divisao_assinatura
# Tabela associativa do N:N entre Assinatura e PessoaVinculada.
# ---------------------------------------------------------------
class DivisaoAssinatura(models.Model):
    id_divisao = models.AutoField(primary_key=True)
    assinatura = models.ForeignKey(Assinatura, on_delete=models.CASCADE,
                                   db_column='id_assinatura', related_name='divisoes')
    pessoa = models.ForeignKey(PessoaVinculada, on_delete=models.CASCADE,
                               db_column='id_pessoa', related_name='divisoes')
    tipo_divisao = models.CharField(max_length=20, default='IGUALITARIA')
    percentual_cota = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        db_table = 'tb_divisao_assinatura'
        verbose_name = 'Divisão de assinatura'
        verbose_name_plural = 'Divisões de assinaturas'

    def __str__(self):
        return f"{self.pessoa.nome} - {self.assinatura.nome_servico} ({self.percentual_cota}%)"

    # Método do nosso diagrama de classes: calcularCotaIgualitaria(numParticipantes)
    # @staticmethod (visto na aula de Python): não usa self, só recebe o parâmetro.
    @staticmethod
    def calcular_cota_igualitaria(num_participantes):
        return (Decimal('100') / num_participantes).quantize(Decimal('0.01'))
