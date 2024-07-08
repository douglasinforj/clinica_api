from rest_framework import viewsets
from clinica_app.models import Cliente, Exame, ExameMarcado
from .serializers import ClienteSerializer, ExameSerializer, ExameMarcadoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    permission_classes = [IsAuthenticated]

    parser_classes = [MultiPartParser, FormParser, JSONParser]         #preparando a classe para receber multipart/form-data, envio de foto

    #garantindo que aceite  metodo Patch  com dados de formulários
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer

    permission_classes = [IsAuthenticated]

class ExameMarcadoViewSet(viewsets.ModelViewSet):
    queryset = ExameMarcado.objects.all()
    serializer_class = ExameMarcadoSerializer

    permission_classes = [IsAuthenticated]




