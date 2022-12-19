from django.shortcuts import render
from django.views import View
from .models import User, UserSettings,Documentation
from django.http import HttpResponseRedirect
from django.urls import reverse
import json


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/index.html")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/login.html")


class CadastroView(View):
    def post(self, request, *args, **kwargs):
        user_name = request.POST.get('user')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        CreationUser = User.objects.create(name=user_name, email=user_email, password=user_password)
        CreationSettings = UserSettings.objects.create(user=CreationUser)
        return HttpResponseRedirect(reverse('mipscode:login'))

    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/cadastro.html")


class DocumentacaoView(View):
    def get(self, request, *args, **kwargs):
        p = Documentation.objects.filter(title='Teste')
        v = p[0].content
        # for line in v:
        #     x = v[line]

        return render(request, "mipscode/documentacao.html",{'tag': v ,'content': v.values() })


class IdeView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "mipscode/ide.html")
