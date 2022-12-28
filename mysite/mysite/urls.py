from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='mipscode/')),
    path('auth/', include('mipscode.urls')),
    path('mipscode/', include('mipscode.urls')),
    path('admin/', admin.site.urls),
]
