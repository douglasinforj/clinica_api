from rest_framework import viewsets
from clinica_app.models import Cliente, Exame, ExameMarcado
from .serializers import ClienteSerializer, ExameSerializer, ExameMarcadoSerializer

from rest_framework.permissions import IsAuthenticated

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    permission_classes = [IsAuthenticated]


class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer

    permission_classes = [IsAuthenticated]

class ExameMarcadoViewSet(viewsets.ModelViewSet):
    queryset = ExameMarcado.objects.all()
    serializer_class = ExameMarcadoSerializer

    permission_classes = [IsAuthenticated]