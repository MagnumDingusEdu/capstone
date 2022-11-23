from uuid import uuid4

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


class Batch(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=1024)

    class Meta:
        verbose_name_plural = 'Batches'

    def __str__(self):
        return self.name


class Branch(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=1024)

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    roll_no = models.PositiveIntegerField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student | {self.user}"

