from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import UserAccount


class Student(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    roll_no = models.PositiveIntegerField()

    def __str__(self):
        return f"Student | {self.user}"


class Scholarship(models.Model):
    class ScholarshipType(models.IntegerChoices):
        MERIT = 1
        MERIT_CUM_MEANS = 2

    name = models.CharField(max_length=200)
    scholarship_type = models.IntegerField(choices=ScholarshipType.choices)

    constraint_class12_percentage = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )

    constraint_class10_percentage = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )

    constraint_cgpa = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )

    notes = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Scholarship | {self.name}"
