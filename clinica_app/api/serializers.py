from rest_framework import serializers
from clinica_app.models import Cliente, Exame, ExameMarcado

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = '__all__'

class ExameMarcadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExameMarcado
        fields = '__all__'