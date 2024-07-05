from django.db import models


class Cliente(models.Model):
    foto = models.ImageField(upload_to='foto_clientes/', blank=True, null=True)
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=12, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    data_nascimento = models.DateField()
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Exame(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    prazos = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class ExameMarcado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    data_exame = models.DateField()
    date_entrega_exame = models.DateField()
    comentarios_resultados = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    documentos_exames = models.FileField(upload_to='documentos_exames/', blank=True, null=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.exame.nome} em {self.data_exame}"