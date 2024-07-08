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

    def create(self, validated_data):
        documentos_exames = validated_data.pop('documentos_exames', None)
        exame_marcado = ExameMarcado.objects.create(**validated_data)
        if documentos_exames:
            exame_marcado.documentos_exames = documentos_exames
            exame_marcado.save()
        return exame_marcado