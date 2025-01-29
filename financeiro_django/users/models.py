from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from django.core.mail import send_mail


class UserManager(BaseUserManager):
    def create_user(self,apelido,primeiro_nome,sobrenome, email, password=None, **extra_fields):    
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            apelido=apelido,
            primeiro_nome=primeiro_nome,
            sobrenome=sobrenome,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, apelido,primeiro_nome,sobrenome, email, password=None, **extra_fields):
        
        user = self.create_user(
            apelido=apelido,
            primeiro_nome=primeiro_nome,
            sobrenome=sobrenome,
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user





class User(AbstractBaseUser, PermissionsMixin):
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    apelido = models.CharField(('apelido'), max_length=30, unique=False, blank=False, null=False)
    primeiro_nome = models.CharField(('primeiro nome'), max_length=30, blank=False, null=False)
    sobrenome = models.CharField(('sobrenome'), max_length=100, blank=False, null=False)
    email = models.EmailField(('e-mail'), max_length=255, unique=True, blank=False, null=False)
    is_staff = models.BooleanField(('staff'), default=False, blank=False, null=False)
    is_active = models.BooleanField(('ativo'), default=True, blank=False, null=False)
    date_joined = models.DateTimeField(('data de cadastro'),auto_now_add=True, blank=False, null=False)
    is_trusty = models.BooleanField(('trusty'), default=False, blank=False, null=False)    
    is_superuser = models.BooleanField(('superuser'), default=False, blank=False, null=False)  
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['apelido', 'primeiro_nome', 'sobrenome']
    
    objects = UserManager()
    
    class Meta:
        verbose_name = ('usuário')
        verbose_name_plural = ('usuários')
    
    def get_full_name(self):
        full_name = '%s %s' % (self.primeiro_nome, self.sobrenome)
        return full_name.strip()
    
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
    
    