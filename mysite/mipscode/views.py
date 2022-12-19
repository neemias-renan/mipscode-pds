from django.shortcuts import get_object_or_404, render
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
        documentation = get_object_or_404(Documentation, pk = kwargs['pk'])
        print(documentation)
        return render(request, "mipscode/documentacao.html",{'document': documentation })


class IdeView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "mipscode/ide.html")
