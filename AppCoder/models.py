from django.db.models import Model
from django.forms import BooleanField, CharField, DateField, EmailField, IntegerField

# class Curso(models.Model) se puede trabajar asi o como arriba con el from django.db.models import Model
# Create your models here.

class Curso(Model):
    nombre = CharField (max_length=40)
    camada = IntegerField()
class Estudiante (Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()

class Profesor (Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    profesion = CharField(max_length=30)
    
class Entregable(Model):
    nombre = CharField(max_length=30)
    fecha_entrega = DateField
    entregado = BooleanField()

    