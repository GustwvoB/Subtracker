from django.urls import path
from . import views

# 'name' é o apelido da rota, usado em {% url 'login' %} e redirect('login')
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # CRUD de assinaturas  (<int:id> captura o número da assinatura na URL)
    path('assinaturas/', views.listar_assinaturas, name='listar_assinaturas'),
    path('assinaturas/nova/', views.cadastrar_assinatura, name='cadastrar_assinatura'),
    path('assinaturas/<int:id>/', views.detalhar_assinatura, name='detalhar_assinatura'),
    path('assinaturas/<int:id>/editar/', views.alterar_assinatura, name='alterar_assinatura'),
    path('assinaturas/<int:id>/excluir/', views.excluir_assinatura, name='excluir_assinatura'),

    # Divisão de custos
    path('assinaturas/<int:id>/divisao/', views.dividir_assinatura, name='dividir_assinatura'),
    path('assinaturas/<int:id>/divisao/<int:id_divisao>/remover/', views.remover_vinculo, name='remover_vinculo'),
]
