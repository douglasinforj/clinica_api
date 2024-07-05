from rest_framework import viewsets
from clinica_app.models import Cliente, Exame, ExameMarcado
from .serializers import ClienteSerializer, ExameSerializer, ExameMarcadoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer

class ExameMarcadoViewSet(viewsets.ModelViewSet):
    queryset = ExameMarcado.objects.all()
    serializer_class = ExameMarcadoSerializer