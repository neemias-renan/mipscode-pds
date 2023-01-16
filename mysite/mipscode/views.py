from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import UserNew, UserSettings, Documentation,Repositorio,Tutorial
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import reverse


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/index.html")

class LoginView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        pass
       

    def get(self, request, *args, **kwargs):
        mensagem = ""
        return render(request, "mipscode/login.html", {'mensagem': mensagem })


class CadastroView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = UserNew.objects.filter(email=email).first()
        
        if user:
            return HttpResponse('Já existe com esse email.')

        CreateUser = UserNew.objects.create(name=username, email=email, password=password)
        CreationSettings = UserSettings.objects.create(user=CreateUser)
        
        return HttpResponseRedirect(reverse('mipscode:login'))

    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/cadastro.html")


class DocumentacaoView(View):
    def get(self, request, *args, **kwargs):
        documentacao = get_object_or_404(Documentation, pk=kwargs['pk'])
        pk = kwargs['pk']
        documentacao_itens = documentacao.content["content"]
        links_documentacao = Documentation.objects.all()
        return render(request, "mipscode/documentacao.html",{"documentacao":documentacao,"documentacao_itens":documentacao_itens,"links_documentacao":links_documentacao})

# {"content": [{"h1": "Tstes de titulo", "p": "A Suprema Corte dos Estados Unidos permitiu nesta segunda-feira que o WhatsApp, da Meta Platforms, abra processo contra a companhia israelense NSO Group por explorar um bug no aplicativo de mensagens para instalar um software de espionagem que permitiu o monitoramento de 1.400 pessoas, incluindo jornalistas, ativistas de direitos humanos e dissidentes."}, {"h1": "Titulo2", "p": "Os juízes rejeitaram recurso da NSO contra decisão de um tribunal inferior que permitiu o andamento do processo. A NSO argumentou que é imune a processos porque agiu como agente de governos estrangeiros não identificados quando instalou o spyware 'Pegasus'."}, {"p": "Em 2019, o WhatsApp processou a NSO buscando uma liminar e indenização, acusando a empresa israelense de acessar os servidores do aplicativo sem permissão para instalar o software Pegasus nos dispositivos móveis das vítimas."}]}



class IdeView(View):
    def get(self, request, *args, **kwargs):
        title_page = "ide"
        return render(request, "mipscode/ide.html",{"title":title_page})
        
class RepositorioView(View):
    def get(self, request, *args, **kwargs):
        user = UserNew.objects.filter(email='teste@gmail.com').first()
        projetos = Repositorio.objects.filter(user=user).order_by('-created_at')
        return render(request, "mipscode/repositorio.html",{'user': user, 'projetos': projetos})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = UserNew.objects.filter(email='teste@gmail.com').first()

        CreateProject = Repositorio.objects.create(user= user,title=title, description=description,content= "null")

        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        user = UserNew.objects.filter(email='teste@gmail.com').first()
        projetos = Repositorio.objects.filter(user=user).order_by('-created_at')[:4]
        tutoriais = Tutorial.objects.all()
        return render(request, "mipscode/dashboard.html",{'user': user, 'projetos': projetos})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = UserNew.objects.filter(email='teste@gmail.com').first()

        CreateProject = Repositorio.objects.create(user= user,title=title, description=description,content= "null")

        return HttpResponseRedirect(reverse('mipscode:dashboard'))


class TutoriaisView(View):
    def get(self, request, *args, **kwargs):
        user = UserNew.objects.filter(email='teste@gmail.com').first()
        projetos = Repositorio.objects.filter(user=user)
        tutoriais = Tutorial.objects.all()
        return render(request, "mipscode/dashboard.html",{'user': user, 'projetos': projetos})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = UserNew.objects.filter(email='teste@gmail.com').first()

        CreateProject = Repositorio.objects.create(user= user,title=title, description=description,content= "null")

        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class AtualizarProjeto(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        projeto = get_object_or_404(Repositorio, pk = kwargs['pk'])

        projeto.title = title
        projeto.description = description
        projeto.save()
        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class RemoverProjeto(View):
    def get(self, request, *args, **kwargs):
        projeto = Repositorio.objects.get(pk = kwargs['pk'])
        projeto.delete()
        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class FavoritarProjeto(View):
    def get(self, request, *args, **kwargs):
        projeto = Repositorio.objects.get(pk = kwargs['pk'])
        projeto.favorite = True
        projeto.save()
        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class DesfavoritarProjeto(View):
    def get(self, request, *args, **kwargs):
        projeto = Repositorio.objects.get(pk = kwargs['pk'])
        projeto.favorite = False
        projeto.save()
        
        return HttpResponseRedirect(reverse('mipscode:repositorio'))



        