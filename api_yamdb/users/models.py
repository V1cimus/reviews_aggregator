from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# For Django version > 3.0
# class UserRole(models.TextChoices):
#    USER = "user", "Пользователь"
#    MODERATOR = "moderator", "Модератор"
#    ADMIN = "admin", "Администратор"

USER_ROLE = (
    ("USER", "user"),
    ("MODERATOR", "moderator"),
    ("ADMIN", "admin")
)


class CustomUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        """Создает и возввращет пользователя с привилегиями суперадмина."""
        user = self._create_user(username, email, password, **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.role = "ADMIN"
        user.save()

        return user


class User(AbstractUser):

    email = models.EmailField("Email", unique=True, null=False)
    bio = models.TextField(
        "Биография",
        blank=True,
        max_length=254,
    )
    role = models.TextField(
        "Роль",
        choices=USER_ROLE,
        default="USER",
    )
    objects = CustomUserManager()

    class Meta:
        ordering = ("id",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"({self.username} - {self.email})"

    @property
    def is_admin(self):
        return (
            self.role == "ADMIN"
            or self.is_staff
            or self.is_superuser
        )

    @property
    def is_moderator(self):
        return self.role == "MODERATOR"

    @property
    def is_user(self):
        return self.role == "USER"
