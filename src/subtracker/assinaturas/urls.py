from django.urls import path
from . import views

# 'name' é o apelido da rota, usado em {% url 'login' %} e redirect('login')
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
