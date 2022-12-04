from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class UserAccount(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    STUDENT = 1
    STAFF = 2

    ROLE_CHOICES = (
        (STUDENT, "Student"),
        (STAFF, "Staff Member"),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)

    class Meta:
        app_label = "accounts"

    def __str__(self):
        return self.email

    def is_student(self):
        return self.role == self.STUDENT

    def is_staff_member(self):
        return self.role == self.STAFF


class Session(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=1024)
    current = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.current:
            return super(Session, self).save(*args, **kwargs)
        with transaction.atomic():
            Session.objects.filter(current=True).update(current=False)
            return super(Session, self).save(*args, **kwargs)


class Student(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student | {self.user}"

    roll_no = models.PositiveIntegerField(blank=True, null=True)
    student_name = models.CharField(max_length=1024, blank=True, null=True)
    father_name = models.CharField(max_length=1024, blank=True, null=True)
    mother_name = models.CharField(max_length=1024, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length=1024, blank=True, null=True)

    current_session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True)
    programme = models.CharField(max_length=1024, blank=True, null=True)
    program_name = models.CharField(max_length=1024, blank=True, null=True)
    branch_code = models.CharField(max_length=1024, blank=True, null=True)
    branch_desc = models.CharField(max_length=1024, blank=True, null=True)

    app_no = models.PositiveIntegerField(blank=True, null=True)
