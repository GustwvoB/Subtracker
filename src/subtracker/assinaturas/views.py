from datetime import date, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import Assinatura, Categoria, PessoaVinculada, DivisaoAssinatura
from .forms import AssinaturaForm, VinculoForm


# ------------------------------------------------------------------
# UC01 - Cadastrar-se
# ------------------------------------------------------------------
def register_view(request):
    # Quem já está logado não precisa ver a tela de cadastro
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        # .get('campo', '') devolve '' se o campo não vier no POST.
        # (request.POST['campo'] daria erro 500 se alguém enviasse o formulário incompleto)
        # .strip() tira espaços das pontas; .lower() deixa o e-mail em minúsculas.
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # validate_email (do próprio Django) levanta ValidationError se o e-mail for inválido
        email_valido = True
        try:
            validate_email(email)
        except ValidationError:
            email_valido = False

        # Validações no servidor, na ordem. A primeira que falhar mostra a mensagem.
        if not nome or not email or not password:
            messages.error(request, 'Preencha todos os campos.')
        elif len(nome) > 150 or len(email) > 150:
            messages.error(request, 'Nome e e-mail devem ter no máximo 150 caracteres.')
        elif not email_valido:
            messages.error(request, 'Informe um e-mail válido.')
        elif len(password) < 8:
            messages.error(request, 'A senha deve ter pelo menos 8 caracteres.')
        elif password != confirm_password:
            messages.error(request, 'A senha e a confirmação não conferem.')
        elif User.objects.filter(username=email).exists():
            # Usamos o e-mail como "username", então basta procurar por ele
            messages.error(request, 'Este e-mail já está cadastrado.')
        else:
            # create_user grava a senha criptografada (hash), nunca em texto puro
            User.objects.create_user(username=email, email=email,
                                     password=password, first_name=nome)
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('login')

        # Se chegou aqui, houve erro: mostra o formulário de novo com o que foi digitado
        return render(request, 'register.html', {'nome': nome, 'email': email})

    return render(request, 'register.html')


# ------------------------------------------------------------------
# UC02 - Fazer Login
# ------------------------------------------------------------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        # authenticate confere e-mail (que é o username) e senha
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # cria a sessão
            return redirect('dashboard')

        # Mensagem genérica: não revela se o e-mail existe ou se a senha é que errou
        messages.error(request, 'E-mail ou senha inválidos.')
        return render(request, 'login.html', {'email': email})

    return render(request, 'login.html')


# ------------------------------------------------------------------
# UC03 - Fazer Logout
# ------------------------------------------------------------------
def logout_view(request):
    logout(request)  # destrói a sessão
    return redirect('login')


# ------------------------------------------------------------------
# UC08 - Dashboard (por enquanto só uma tela de boas-vindas)
# ------------------------------------------------------------------
@login_required(login_url='login')  # sem login, manda para a tela de login
def dashboard(request):
    return render(request, 'assinaturas/dashboard.html', {})


# Função auxiliar usada pelas views que recebem o número (id) de uma assinatura na URL.
# Devolve a assinatura SE ela existir e for do usuário logado; senão, erro 404.
def buscar_assinatura_do_usuario(request, id):
    # Um número gigante na URL estouraria o banco de dados (erro 500).
    # 2147483647 é o maior número inteiro aceito pelo banco: acima disso, "não existe".
    if id > 2147483647:
        raise Http404
    return get_object_or_404(Assinatura, pk=id, usuario=request.user)


# ------------------------------------------------------------------
# UC07 - Consultar/Buscar Assinaturas
# ------------------------------------------------------------------
@login_required(login_url='login')
def listar_assinaturas(request):
    # SEMPRE filtramos pelo usuário logado: ninguém vê assinatura de outra pessoa
    assinaturas = Assinatura.objects.filter(usuario=request.user)

    # Parâmetros da busca vêm pela URL (GET): ?busca=net&categoria=1&status=vencendo
    busca = request.GET.get('busca', '').strip()
    categoria_id = request.GET.get('categoria', '')
    status = request.GET.get('status', '')

    # 1) Busca por nome (icontains = "contém", sem diferenciar maiúsculas/minúsculas)
    if busca:
        assinaturas = assinaturas.filter(nome_servico__icontains=busca)

    # 2) Filtro por categoria (isdigit evita erro se alguém digitar texto na URL;
    #    limitar a 9 dígitos evita um número gigante que estouraria o banco)
    if categoria_id.isdigit() and len(categoria_id) <= 9:
        categoria_id = int(categoria_id)
        assinaturas = assinaturas.filter(categoria=categoria_id)
    else:
        categoria_id = None

    # 3) Filtro por status de vencimento (gte = maior ou igual, lte = menor ou igual, lt = menor)
    hoje = date.today()
    if status == 'vencendo':
        assinaturas = assinaturas.filter(data_vencimento__gte=hoje,
                                         data_vencimento__lte=hoje + timedelta(days=7))
    elif status == 'vencidas':
        assinaturas = assinaturas.filter(data_vencimento__lt=hoje)
    elif status == 'trial':
        assinaturas = assinaturas.filter(eh_free_trial=True)
    else:
        status = ''

    contexto = {
        'assinaturas': assinaturas,
        'categorias': Categoria.objects.all(),   # para montar o <select> de categorias
        'busca': busca,
        'categoria_id': categoria_id,
        'status': status,
        'filtrando': bool(busca or categoria_id or status),
    }
    return render(request, 'assinaturas/listar_assinaturas.html', contexto)


# Detalhes de uma assinatura
@login_required(login_url='login')
def detalhar_assinatura(request, id):
    # se não existir OU for de outro usuário, devolve página 404
    assinatura = buscar_assinatura_do_usuario(request, id)
    return render(request, 'assinaturas/detalhar_assinatura.html', {'assinatura': assinatura})


# ------------------------------------------------------------------
# UC04 - Cadastrar Assinatura
# ------------------------------------------------------------------
@login_required(login_url='login')
def cadastrar_assinatura(request):
    if request.method == 'POST':
        # A assinatura já nasce com o dono (usuário logado) via instance=
        form = AssinaturaForm(request.POST, instance=Assinatura(usuario=request.user))
        if form.is_valid():
            form.save()
            messages.success(request, 'Assinatura cadastrada com sucesso.')
            return redirect('listar_assinaturas')
        messages.error(request, 'Erro no preenchimento do formulário. Verifique os dados informados.')
    else:
        form = AssinaturaForm()
    return render(request, 'assinaturas/form_assinatura.html', {'form': form})


# ------------------------------------------------------------------
# UC05 - Editar Assinatura
# ------------------------------------------------------------------
@login_required(login_url='login')
def alterar_assinatura(request, id):
    assinatura = buscar_assinatura_do_usuario(request, id)
    if request.method == 'POST':
        form = AssinaturaForm(request.POST, instance=assinatura)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assinatura alterada com sucesso.')
            return redirect('listar_assinaturas')
        messages.error(request, 'Erro ao alterar a assinatura. Verifique os dados informados.')
    else:
        form = AssinaturaForm(instance=assinatura)   # formulário já preenchido
    return render(request, 'assinaturas/form_assinatura.html',
                  {'form': form, 'editar': True, 'assinatura': assinatura})


# ------------------------------------------------------------------
# UC06 - Excluir Assinatura (com tela de confirmação)
# ------------------------------------------------------------------
@login_required(login_url='login')
def excluir_assinatura(request, id):
    assinatura = buscar_assinatura_do_usuario(request, id)
    if request.method == 'POST':
        assinatura.delete()
        messages.success(request, 'Assinatura excluída com sucesso.')
        return redirect('listar_assinaturas')
    return render(request, 'assinaturas/excluir_assinatura.html', {'assinatura': assinatura})

# ------------------------------------------------------------------
# UC09 - Vincular Pessoa a uma Assinatura (Divisão de Custo)
# ------------------------------------------------------------------
@login_required(login_url='login')
def dividir_assinatura(request, id):
    assinatura = buscar_assinatura_do_usuario(request, id)

    if request.method == 'POST':
        form = VinculoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']   # vem '' quando não é informado

            # Reaproveita um contato que ESTE usuário já tenha, para não duplicar pessoas:
            # - se informou e-mail, procura pelo e-mail;
            # - se não informou, procura pelo nome (iexact = igual, sem diferenciar maiúsculas).
            if email:
                pessoa = PessoaVinculada.objects.filter(usuario_dono=request.user, email__iexact=email).first()
            else:
                pessoa = PessoaVinculada.objects.filter(usuario_dono=request.user, nome__iexact=nome).first()

            # Não achou: cadastra uma nova pessoa para este usuário
            if pessoa is None:
                pessoa = PessoaVinculada.objects.create(usuario_dono=request.user, nome=nome,
                                                        email=email or None)

            if DivisaoAssinatura.objects.filter(assinatura=assinatura, pessoa=pessoa).exists():
                messages.error(request, 'Essa pessoa já participa da divisão desta assinatura.')
            else:
                DivisaoAssinatura.objects.create(assinatura=assinatura, pessoa=pessoa,
                                                 tipo_divisao='IGUALITARIA')
                assinatura.recalcular_divisoes()   # a cota de todos muda quando entra mais alguém
                messages.success(request, 'Pessoa vinculada com sucesso.')
                return redirect('dividir_assinatura', id=assinatura.pk)
        else:
            messages.error(request, 'Erro no preenchimento do formulário. Verifique os dados informados.')
    else:
        form = VinculoForm()

    return render(request, 'assinaturas/dividir_assinatura.html',
                  {'assinatura': assinatura, 'form': form})


# Remove uma pessoa da divisão (só aceita POST, que vem com o token CSRF)
@login_required(login_url='login')
def remover_vinculo(request, id, id_divisao):
    assinatura = buscar_assinatura_do_usuario(request, id)
    if id_divisao > 2147483647:   # mesma proteção contra número gigante na URL
        raise Http404
    # a divisão precisa pertencer a ESTA assinatura (que já é do usuário logado)
    divisao = get_object_or_404(DivisaoAssinatura, pk=id_divisao, assinatura=assinatura)

    if request.method == 'POST':
        divisao.delete()
        assinatura.recalcular_divisoes()   # os que ficaram passam a pagar mais
        messages.success(request, 'Pessoa removida da divisão.')
    return redirect('dividir_assinatura', id=assinatura.pk)
