from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
  def create_user(self, username, password=None):
    
    if not username:
        raise ValueError('Users must have an username')
    user = self.model(username=username)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, password):
    
    user = self.create_ser(
      username=username,
      password=password,
      )
    user.is_admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser, PermissionsMixin):
      id = models.BigAutoField(primary_key=True)
      rol=models.CharField('Rol', max_length=50)
      username = models.CharField('Username', max_length = 15, unique=True)
      password = models.CharField('Password', max_length = 256)
      nombre = models.CharField('Nombre', max_length = 50)
      identificacion=models.CharField('Identificacion', max_length = 50)
      email = models.EmailField('Email', max_length = 100)
      apellido= models.CharField('Apellido', max_length = 50)
      fecha_nacimiento = models.CharField('Fecha_nacimiento', max_length = 15)
      direccion = models.CharField('Direccion', max_length = 30)
      ciudad = models.CharField('Ciudad', max_length = 20)
      numero_telefonico = models.CharField('Numero_telefonico', max_length = 30)
      
      def save(self, **kwargs):
            some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
            self.password = make_password(self.password, some_salt)
            super().save(**kwargs)
      
      objects = UserManager()
      USERNAME_FIELD = 'username'
      
