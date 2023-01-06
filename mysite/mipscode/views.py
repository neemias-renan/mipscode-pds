from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .models import Profile, ProfileSettings, Documentation, Repositorio, Tutorial
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import reverse


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/index.html")

class LoginView(TemplateView):
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        print(request.POST)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user)
            return HttpResponseRedirect(reverse('mipscode:index'))
        else:
            context = { 'msg': 'Usuário ou senha incorretos!'}
            print('deu erro')
            return render(request, "mipscode/login.html", context)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = { 'msg': 'Usuário já está autenticado' }
            print('usuário já está autenticado')
            logout(request)
            return render(request, 'mipscode/login.html', context)

        mensagem = ""
        return render(request, "mipscode/login.html", {'mensagem': mensagem })

def LogoutView(request):
    logout(request)

class CadastroView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/cadastro.html")

    def post(self, request, *args, **kwargs):
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']

        userExists = User.objects.filter(email=email).first()
        
        if userExists:
            return HttpResponse('Já existe com esse email.')

        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(user=user)
        user.save()
        profile.save()
        
        return HttpResponseRedirect(reverse('mipscode:login'))
        




class DocumentacaoView(TemplateView):
    def get(self, request, *args, **kwargs):
        documentation = get_object_or_404(Documentation, pk = kwargs['pk'])
        print(documentation)
        return render(request, "mipscode/documentacao.html",{'document': documentation })


class IdeView(TemplateView):
    def get(self, request, *args, **kwargs):

        return render(request, "mipscode/ide.html")
        
class RepositorioView(TemplateView):
    def get(self, request, *args, **kwargs):
        user = Profile.objects.filter(email='teste@gmail.com').first()
        projetos = Repositorio.objects.filter(user=user).order_by('-created_at')
        return render(request, "mipscode/repositorio.html",{'user': user, 'projetos': projetos})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = Profile.objects.filter(email='teste@gmail.com').first()

        CreateProject = Repositorio.objects.create(user= user,title=title, description=description,content= "null")

        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class DashboardView(TemplateView):
    def get(self, request, *args, **kwargs):
        user = Profile.objects.filter(email='teste@gmail.com').first()
        projetos = Repositorio.objects.filter(user=user).order_by('-created_at')[:4]
        tutoriais = Tutorial.objects.all()
        return render(request, "mipscode/dashboard.html",{'user': user, 'projetos': projetos})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = Profile.objects.filter(email='teste@gmail.com').first()

        CreateProject = Repositorio.objects.create(user= user,title=title, description=description,content= "null")

        return HttpResponseRedirect(reverse('mipscode:dashboard'))


class TutoriaisView(TemplateView):
    def get(self, request, *args, **kwargs):
        user = Profile.objects.filter(email='teste@gmail.com').first()
        projetos = Repositorio.objects.filter(user=user)
        tutoriais = Tutorial.objects.all()
        return render(request, "mipscode/dashboard.html",{'user': user, 'projetos': projetos})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = Profile.objects.filter(email='teste@gmail.com').first()

        CreateProject = Repositorio.objects.create(user= user,title=title, description=description,content= "null")

        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class AtualizarProjeto(TemplateView):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        projeto = get_object_or_404(Repositorio, pk = kwargs['pk'])

        projeto.title = title
        projeto.description = description
        projeto.save()
        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class RemoverProjeto(TemplateView):
    def get(self, request, *args, **kwargs):
        projeto = Repositorio.objects.get(pk = kwargs['pk'])
        projeto.delete()
        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class FavoritarProjeto(TemplateView):
    def get(self, request, *args, **kwargs):
        projeto = Repositorio.objects.get(pk = kwargs['pk'])
        projeto.favorite = True
        projeto.save()
        return HttpResponseRedirect(reverse('mipscode:repositorio'))

class DesfavoritarProjeto(TemplateView):
    def get(self, request, *args, **kwargs):
        projeto = Repositorio.objects.get(pk = kwargs['pk'])
        projeto.favorite = False
        projeto.save()
        
        return HttpResponseRedirect(reverse('mipscode:repositorio'))



        