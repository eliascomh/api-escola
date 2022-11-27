from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=11)
    cpf = models.CharField(max_length=10)
    data_de_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    NIVEL = {
        ('B', 'Básico'),
        ('I', 'Itermediário'),
        ('A', 'Avançado')
    }

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao