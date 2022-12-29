from django.urls import path

from . import views

app_name = 'mipscode'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    # path('documentacao/', views.DocumentacaoView.as_view(), name='documentacao'),
    path('documentacao/<int:pk>/', views.DocumentacaoView.as_view(), name='documentacao'),
    path('ide/', views.IdeView.as_view(), name='ide'),
    path('projeto/', views.ProjetoView.as_view(), name='projeto'),
    path('projeto/<int:pk>/atualizar', views.AtualizarProjeto.as_view(), name='atualizarprojeto'),
    path('projeto/<int:pk>/remover', views.RemoverProjeto.as_view(), name='removerprojeto'),
    path('projeto/<int:pk>/favoritar', views.FavoritarProjeto.as_view(), name='favoritarprojeto'),
    path('projeto/<int:pk>/desfavoritar', views.DesfavoritarProjeto.as_view(), name='desfavoritarprojeto'),


]