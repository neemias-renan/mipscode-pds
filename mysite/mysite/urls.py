from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mipscode/', include('mipscode.urls')),
    path('admin/', admin.site.urls),
]
