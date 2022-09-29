from django.contrib import admin
from .models.user import User
from .models.medico import Medico
from .models.paciente import Paciente
from .models.enfermero import Enfermero

admin.site.register(User)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Enfermero)