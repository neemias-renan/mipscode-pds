from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/index.html")

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/login.html")
    
class CadastroView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/cadastro.html")
    
class DocumentacaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/documentacao.html")

class IdeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mipscode/ide.html")