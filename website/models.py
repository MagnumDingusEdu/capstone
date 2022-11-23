from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import UserAccount, Student

STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman & Diu', 'Dadra and Nagar Haveli and Daman & Diu'),
    ('The Government of NCT of Delhi', 'The Government of NCT of Delhi'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
)


class Constraint(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Scholarship(models.Model):
    class ScholarshipType(models.IntegerChoices):
        MERIT = 1
        MERIT_CUM_MEANS = 2

    name = models.CharField(max_length=200)
    scholarship_type = models.IntegerField(choices=ScholarshipType.choices)
    enabled = models.BooleanField(default=True)

    amount = models.CharField(max_length=1024)

    notes = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    constraints = models.ManyToManyField(Constraint, through="ScholarshipConstraint")

    def __str__(self):
        return f"Scholarship | {self.name}"


class ScholarshipConstraint(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    constraint = models.ForeignKey(Constraint, on_delete=models.CASCADE)
    min_value = models.FloatField(blank=True, null=True)
    max_value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.constraint.name} constraint on [{self.scholarship.name}]"


class McmApplication(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    contact_number = models.PositiveIntegerField()
    alternate_contact_number = models.PositiveIntegerField()
    state_of_residence = models.CharField(choices=STATE_CHOICES, max_length=255)
    twelfth_marks = models.CharField(max_length=255)
    current_cgpa_or_rank = models.CharField(max_length=255)
    family_income = models.CharField(max_length=255)
    # TODO: fill more fields, https://docs.google.com/forms/d/e/1FAIpQLScSaU3NGIu13V4j9fEi5B1Djl503c72o9sZ-9YsVY1_hsM4aA/viewform
