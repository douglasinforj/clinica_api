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

#adicionadno Swagger ao projeto:

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Clinica API",
      default_version='v1',
      description="Documentação da API para gerenciamento de clientes e exames",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="douglasitpro@gmail.com"),
      license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

#rota de autenticação:

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



# rotas urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #rotas de autenticação
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





