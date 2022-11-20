from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class UserAccount(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    STUDENT = 1
    STAFF = 2

    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (STAFF, 'Staff Member'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)

    class Meta:
        app_label = 'accounts'

    def __str__(self):
        return (self.first_name + " " + self.last_name).strip() or self.email

    def is_student(self):
        return self.role == self.STUDENT

    def is_staff_member(self):
        return self.role == self.STAFF
