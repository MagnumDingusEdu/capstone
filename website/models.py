from uuid import uuid4
from django.db import models

from accounts.models import UserAccount


class Student(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    roll_no = models.PositiveIntegerField()

    def __str__(self):
        return f"Student | {self.user}"
