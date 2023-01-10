import uuid
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.common.media_path import profile_avatar_path


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True,  upload_to=profile_avatar_path,  default="/images/profiles/profile_default.png",)
    country = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    account_activation_otp = models.CharField(max_length=255, blank=True, null=True, unique=True)
    reset_password_otp = models.CharField(max_length=255, blank=True, null=True, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

