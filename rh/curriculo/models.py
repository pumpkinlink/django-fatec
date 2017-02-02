from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    datacadastro = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.nome


class Curriculo(models.Model):
    arquivo = models.FileField()
    datacadastro = models.DateTimeField(auto_now_add=True)
    aluno = models.ForeignKey(Aluno, unique=True)

    def __unicode__(self):
        return 'Curriculo: %s' % self.id
