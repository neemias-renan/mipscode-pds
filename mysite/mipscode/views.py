from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import UserNew, UserSettings, Documentation,Project
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
        print(documentation)
        return render(request, "mipscode/documentacao.html",{'document': documentation })


class IdeView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "mipscode/ide.html")
        
class ProjetoView(View):
    def get(self, request, *args, **kwargs):
        user = UserNew.objects.filter(email='teste@gmail.com').first()
        projetos = Project.objects.filter(user=user)
        return render(request, "mipscode/projeto.html",{'user': user, 'projetos': projetos})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = UserNew.objects.filter(email='teste@gmail.com').first()

        CreateProject = Project.objects.create(user= user,title=title, description=description,content= "null")

        return HttpResponseRedirect(reverse('mipscode:projeto'))

class AtualizarProjeto(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        projeto = get_object_or_404(Project, pk = kwargs['pk'])

        projeto.title = title
        projeto.description = description
        projeto.save()
        return HttpResponseRedirect(reverse('mipscode:projeto'))

class RemoverProjeto(View):
    def get(self, request, *args, **kwargs):
        projeto = Project.objects.get(pk = kwargs['pk'])
        projeto.delete()
        return HttpResponseRedirect(reverse('mipscode:projeto'))

class FavoritarProjeto(View):
    def get(self, request, *args, **kwargs):
        projeto = Project.objects.get(pk = kwargs['pk'])
        projeto.favorite = True
        projeto.save()
        return HttpResponseRedirect(reverse('mipscode:projeto'))

class DesfavoritarProjeto(View):
    def get(self, request, *args, **kwargs):
        projeto = Project.objects.get(pk = kwargs['pk'])
        projeto.favorite = False
        projeto.save()
        
        return HttpResponseRedirect(reverse('mipscode:projeto'))



        