from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            is_active=is_active,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'document_number'

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'email',
        'mobile_number',
    ]

    email = models.EmailField(
        unique=True,
        verbose_name='Correo electrónico',
    )

    first_name = models.CharField(
        max_length=128,
        verbose_name='nombre',
    )

    last_name = models.CharField(
        max_length=128,
        verbose_name='apellido',
    )

    document_number = models.CharField(
        unique=True,
        max_length=12,
        verbose_name='número de documento',
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name='staff',
        help_text='Indica si puede entrar al sitio de administración.',
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name='activo',
        help_text='Indica si el usuario puede ingresar a la plataforma.',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de registro',
    )

    objects = UserManager()

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-id']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
