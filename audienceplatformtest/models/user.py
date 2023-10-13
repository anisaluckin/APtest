from django.contrib.auth import models as auth_models
from django.db import models
from django.contrib.auth.hashers import make_password


class UserManager(auth_models.BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email address must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        app_label = "audienceplatformtest"
        indexes = [
            models.Index(fields=['id', ]),
        ]