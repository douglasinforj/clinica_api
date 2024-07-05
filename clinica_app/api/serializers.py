from rest_framework import serializers
from clinica_app.models import Cliente, Exame, ExameMarcado

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class ExameMarcadoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'