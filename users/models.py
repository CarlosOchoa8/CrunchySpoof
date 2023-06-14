from django.db import models, transaction
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, **extra_fields):
        email = self.normalize_email(email)
        extra_fields.update({'email': email})
        password = extra_fields.get('password')
        user = self.model(**extra_fields)
        user.set_password(password)
        with transaction.atomic():
            user.save()
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    # email = models.EmailField(max_length=50, unique=True, null=False)
    # username = models.CharField(max_length=50)
    is_premium = models.BooleanField(verbose_name='Es usuario premium')
    premium_type = models.CharField(max_length=20, verbose_name='Tipo de suscripción', default=None)
