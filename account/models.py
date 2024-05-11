from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from elikiba.models import BaseModel
from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    # User info
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    profile_image = models.FileField(upload_to='user', null=True, blank=True)

    # Login fields
    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff  # Modify as needed based on your permission logic

    def has_module_perms(self, app_label):
        return True  # Modify as needed based on your permission logic

    def is_admin(self):
        return self.is_staff

    @property
    def is_name_added(self):
        if self.first_name and self.last_name:
            return True
        return False

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
