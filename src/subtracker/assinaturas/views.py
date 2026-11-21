from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


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
