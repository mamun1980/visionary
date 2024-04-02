from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where membership_number is the unique identifiers
    for authentication.
    """

    def create_user(self, email, phone=None, name=None, password=None, **extra_fields):
        """
        Create and save a User with given membership_number and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, phone=None, name=None, password=None, **extra_fields
    ):
        """
        Create and save a SuperUser with the given membership_number and password.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, phone, name, password, **extra_fields)


class VisionaryUser(AbstractUser):
    """
    Custom user model.
    """
    username = None
    phone = models.CharField(_('Phone number'), max_length=17, unique=True, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True, blank=False, null=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True)
    last_name = models.CharField(_("last Name"), max_length=150, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
