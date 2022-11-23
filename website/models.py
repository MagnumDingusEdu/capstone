from uuid import uuid4

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


class MCMApp(models.Model):
    # TODO: add verbose_name

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    contact_number = models.PositiveIntegerField()
    alternate_contact_number = models.PositiveIntegerField()
    state_of_residence = models.CharField(choices=STATE_CHOICES, max_length=255)

    class_12_marks = models.CharField(max_length=255)  # % or CGPA
    current_cgpa_or_rank = models.CharField(max_length=255,
                                            help_text="Current CGPA or Rank or Diploma %")

    family_income_per_mcm_application = models.CharField(max_length=255,
                                                         help_text="FAMILY INCOME AS MENTIONED IN MCM APPLICATION FORM")
    family_income_per_affidavit = models.CharField(max_length=255,
                                                   help_text="FAMILY INCOME AS PER AFFIDAVIT ATTACHED")
    family_income_per_certificate = models.CharField(max_length=255,
                                                     help_text="FAMILY INCOME AS PER CERTIFICATE OF TEHSILDAR")
    bank_balance = models.IntegerField()
    fdr_balance = models.CharField(max_length=255, help_text="")

    itr_annual_year_current = models.IntegerField(help_text="ITR for this annual year")
    itr_annual_year_last = models.IntegerField(help_text="ITR for previous annual year")
    itr_annual_year_last_last = models.IntegerField(help_text="ITR for last to last annual year")

    immovable_property = models.BooleanField(help_text="IMMOVABLE PROPERTY AS PER AFFIDAVIT")
    single_girl_child = models.BooleanField(help_text="Are you a Single Girl Child?")

    applied_for_mcp_special = models.BooleanField(help_text="APPLIED FOR MCM SPECIAL?")
    mcp_special_reason = models.TextField(help_text="SPECIFIC REASON FOR APPLYING MCM SPECIAL?")

    applied_for_other_scholarship = models.BooleanField(help_text="HAVE YOU APPLIED FOR ANY OTHER SCHOLARSHIP?")
    other_scholarship_details = models.TextField(help_text="DETAILS OF OTHER SCHOLARSHIP APPLIED")

    previous_year_scholarship = models.BooleanField(
        help_text="HAVE YOU RECEIVED ANY SCHOLARSHIP IN THE PREVIOUS YEAR?")
    previous_year_scholarship_details = models.TextField(help_text="DETAILS OF PREVIOUS SCHOLARSHIP RECEIVED")
    previous_year_scholarship_amount = models.IntegerField(help_text="AMOUNT OF THE PREVIOUS SCHOLARSHIP")

    # TODO: upload documents

    declaration = models.BooleanField(
        help_text="I ACKNOWLEDGE THAT I HAVE READ ALL THE ELIGIBILITY CRITERIA OF SCHOLARSHIP AND I AM ELIGIBLE FOR "
                  "APPLYING TIET MERIT CUM MEANS SCHOLARSHIP.")

    # TODO: fill more fields, https://docs.google.com/forms/d/e/1FAIpQLScSaU3NGIu13V4j9fEi5B1Djl503c72o9sZ-9YsVY1_hsM4aA/viewform


class NoticeCategory(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    title = models.TextField()
    collapsed = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Notice Categories"


class Notice(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    category = models.ForeignKey(NoticeCategory, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField()
    attachment = models.FileField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title
