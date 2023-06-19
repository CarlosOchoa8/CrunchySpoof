from django.db import models, transaction
from django.contrib.auth.models import BaseUserManager, AbstractUser


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
    profile_image = models.ImageField('users/profile', null=True, blank=True)
    profile_cover = models.ImageField('users/profile', null=True, blank=True)
    is_premium = models.BooleanField(verbose_name='Es usuario premium', default=False)
    premium_type = models.CharField(max_length=20, verbose_name='Tipo de suscripción', default='Free')
