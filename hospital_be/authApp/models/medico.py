from django.db import models
from .user import User

class Medico(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    especialidad=models.CharField('especialidad', max_length=100)