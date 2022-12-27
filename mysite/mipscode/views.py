from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import User, UserSettings, Documentation
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/index.html")


class LoginView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            
            login_django(request, user)
            return redirect(reverse('mipscode:projeto'))
            # messages.success(request, f' welcome {username} !!')
            # return redirect('index')
            # return HttpResponse(user.email)
            # return HttpResponseRedirect(reverse('mipscode:projeto'))
        else:
            mensagem = "Email ou Senha não encontrados"
            return render(request, "mipscode/login.html", {'mensagem': mensagem })

    def get(self, request, *args, **kwargs):
        mensagem = ""
        return render(request, "mipscode/login.html", {'mensagem': mensagem })


class CadastroView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        
        if user:
            return HttpResponse('Já existe com esse email.')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        # CreationSettings = UserSettings.objects.create(user=user)
        
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
        user = request.user
        return render(request, "mipscode/projeto.html",{'user': user })
        # return HttpResponse('faça login')