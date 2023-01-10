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
        documentation = get_object_or_404(Documentation, pk = kwargs['pk'])
        title = documentation.title
        print(documentation.values())
        return render(request, "mipscode/documentacao.html",{'title':title,'document': documentation })


class IdeView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "mipscode/ide.html")
        
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



        