from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.users.forms import LoginForms, CadastroForms
from apps.users.models import PerfilUsuario
import folium
from django.contrib import messages

def login(request):
    form = LoginForms()
    
    if request.method == "POST":
        form = LoginForms(request.POST)
        
        if form.is_valid():
            # Extrair dados do formulário
            nome_login = form.cleaned_data.get("nome_login")
            senha = form.cleaned_data.get("senha_1")
            
            # Autenticar o usuário usando o nome de login e senha
            user = authenticate(request, username=nome_login, password=senha)
            
            if user is not None:
                # Login bem-sucedido
                auth_login(request, user)
                return redirect("index")  # Redireciona para a página principal
            else:
                # Se a autenticação falhar, exibir mensagem de erro
                messages.error(request, "Nome de usuário ou senha incorretos.")
                return redirect("login")
    
    # Renderiza o formulário caso o método não seja POST
    return render(request, 'apps/users/login.html', {"form": form})

def registro(request):
    form = CadastroForms()
    
    if request.method == "POST":
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha_1"]. value() != form["senha_2"]. value():
                return redirect("registro")
            
            nome = form["nome_cadastro"]. value()
            email = form["email"]. value()
            telefone = form["telefone"]. value()
            data_nascimento = form["data_nascimento"]. value()
            senha = form["senha_1"]. value()
            tipo_doc = form["tipo_doc"]. value()
            documento = form["documento"]. value()
            
            if User.objects.filter(username=nome).exists():
                return redirect("registro")
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            
            # Criar o perfil do usuário no modelo PerfilUsuario
            perfil_usuario = PerfilUsuario.objects.create(
                usuario=usuario,
                telefone=telefone,
                data_nascimento=data_nascimento,
                tipo_doc=tipo_doc,
                documento=documento
            )
            
            # Salvar ambos os objetos
            usuario.save()
            perfil_usuario.save()
            return redirect("login")
    
    return render(request, 'apps/users/registro.html', {"form": form})

def perfil(request):
    return render(request, 'apps/users/perfil.html')