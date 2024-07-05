"""
URL configuration for clinica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#router
from rest_framework.routers import DefaultRouter

#importando as viwessets
from clinica_app.api.viewsets import ClienteViewSet, ExameViewSet, ExameMarcadoViewSet

#Arquivos de mídia
from django.conf import settings
from django.conf.urls.static import static

#rotas
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'exames', ExameViewSet)
router.register(r'exames-marcados', ExameMarcadoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
