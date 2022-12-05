import dataclasses
from uuid import uuid4

from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    FileExtensionValidator,
)
from django.db import models

from accounts.models import UserAccount, Student, Session

STATE_CHOICES = (
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttarakhand", "Uttarakhand"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    (
        "Dadra and Nagar Haveli and Daman & Diu",
        "Dadra and Nagar Haveli and Daman & Diu",
    ),
    ("The Government of NCT of Delhi", "The Government of NCT of Delhi"),
    ("Jammu & Kashmir", "Jammu & Kashmir"),
    ("Ladakh", "Ladakh"),
    ("Lakshadweep", "Lakshadweep"),
    ("Puducherry", "Puducherry"),
)


class Constraint(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True, null=True)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ScholarshipCategory(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Scholarship Categories"


class Scholarship(models.Model):
    class ScholarshipType(models.IntegerChoices):
        # NOTE: don't change the integer values
        MCM_TIET = 1
        MCM_ALUMNI = 2
        MCM_OTHER = 3
        MERIT_ALUMNI = 4
        MERIT_AUTO = 5

    name = models.CharField(max_length=200)
    category = models.ForeignKey(ScholarshipCategory, on_delete=models.CASCADE)
    scholarship_type = models.IntegerField(choices=ScholarshipType.choices)

    eligibility_criteria = models.TextField()
    number_of_scholarships = models.CharField(max_length=1024)
    value_of_scholarship = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    constraints = models.ManyToManyField(Constraint, through="ScholarshipConstraint")

    def __str__(self):
        return self.name

    @property
    def verbose_type(self):
        if self.scholarship_type == 1:
            return "MCM_TIET"
        elif self.scholarship_type == 2:
            return "MCM_ALUMNI"
        elif self.scholarship_type == 3:
            return "MCM_OTHER"
        elif self.scholarship_type == 4:
            return "MERIT_ALUMNI"
        else:
            return "MERIT_AUTO"


class ScholarshipConstraint(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    constraint = models.ForeignKey(Constraint, on_delete=models.CASCADE)
    min_value = models.FloatField(blank=True, null=True)
    max_value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.constraint.name} constraint on [{self.scholarship.name}]"


class MCMTietApplication(models.Model):
    """Scholarship Type: MCM_TIET = 1"""

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    contact_number = models.PositiveIntegerField()
    alternate_contact_number = models.PositiveIntegerField()
    state_of_residence = models.CharField(choices=STATE_CHOICES, max_length=255)

    class_12_marks = models.CharField(
        max_length=255, help_text="Enter percentage e.g. 89.8 "
    )  # % or CGPA
    current_cgpa_or_rank = models.CharField(
        max_length=255, help_text="Current CGPA or Rank or Diploma %"
    )

    family_income_per_mcm_application = models.CharField(
        max_length=255, help_text="FAMILY INCOME AS MENTIONED IN MCM APPLICATION FORM"
    )
    family_income_per_affidavit = models.CharField(
        max_length=255, help_text="FAMILY INCOME AS PER AFFIDAVIT ATTACHED"
    )
    family_income_per_certificate = models.CharField(
        max_length=255, help_text="FAMILY INCOME AS PER CERTIFICATE OF TEHSILDAR"
    )
    bank_balance = models.IntegerField()
    fdr_balance = models.CharField(max_length=255, help_text="")

    itr_annual_year_current = models.IntegerField(help_text="ITR for this annual year")
    itr_annual_year_last = models.IntegerField(help_text="ITR for previous annual year")
    itr_annual_year_last_last = models.IntegerField(
        help_text="ITR for last to last annual year"
    )

    immovable_property = models.BooleanField(
        help_text="IMMOVABLE PROPERTY AS PER AFFIDAVIT"
    )
    single_girl_child = models.BooleanField(help_text="Are you a Single Girl Child?")

    applied_for_mcp_special = models.BooleanField(help_text="APPLIED FOR MCM SPECIAL?")
    mcp_special_reason = models.TextField(
        help_text="SPECIFIC REASON FOR APPLYING MCM SPECIAL?", blank=True, null=True
    )

    applied_for_other_scholarship = models.BooleanField(
        help_text="HAVE YOU APPLIED FOR ANY OTHER SCHOLARSHIP?"
    )
    other_scholarship_details = models.TextField(
        help_text="DETAILS OF OTHER SCHOLARSHIP APPLIED", blank=True, null=True
    )

    previous_year_scholarship = models.BooleanField(
        help_text="HAVE YOU RECEIVED ANY SCHOLARSHIP IN THE PREVIOUS YEAR?"
    )
    previous_year_scholarship_details = models.TextField(
        help_text="DETAILS OF PREVIOUS SCHOLARSHIP RECEIVED", blank=True, null=True
    )
    previous_year_scholarship_amount = models.IntegerField(
        help_text="AMOUNT OF THE PREVIOUS SCHOLARSHIP", blank=True, null=True
    )

    income_certificate = models.FileField(
        help_text="Please upload a digital / scanned copy of your income certificate",
        upload_to="income_certificates",
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf", "jpg", "png", "jpeg"])
        ],
    )
    supporting_documents = models.FileField(
        help_text="Please upload supporting documents in a .zip format, if any",
        blank=True,
        null=True,
        upload_to="supporting_documents",
    )

    declaration = models.BooleanField(
        help_text="I acknowledge that i have read all the eligibility criteria of scholarship and i am eligible for "
                  "applying to TIET Merit-cum-means scholarship."
    )

    status = models.CharField(
        max_length=1024,
        default="PENDING",
        choices=(
            ("PENDING", "PENDING"),
            ("APPROVED", "APPROVED"),
            ("REJECTED", "REJECTED"),
        ),
    )
    remarks = models.TextField(blank=True, null=True)

    # TODO: fill more fields, https://docs.google.com/forms/d/e/1FAIpQLScSaU3NGIu13V4j9fEi5B1Djl503c72o9sZ-9YsVY1_hsM4aA/viewform

    def __str__(self):
        return f"Application for [{self.scholarship.name[:15]}...]"

    class Meta:
        verbose_name_plural = "Merit cum Means Applications"
        verbose_name = "Merit cum means Application"


class MCMAlumniApplication(models.Model):
    """Scholarship Type: MCM_ALUMNI = 2"""

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)

    photograph = models.FileField(
        help_text="Passport size photograph in JPG/PNG under 2 MB.",
        blank=True,
        null=True,
        upload_to="photographs",
    )

    roll_no = models.CharField(max_length=20, help_text="Registration/Roll No")
    personal_contact_number = models.PositiveIntegerField()
    year = models.CharField(max_length=20, help_text="Year")
    branch = models.CharField(max_length=20, help_text="Branch")

    jee_main_rank = models.CharField(max_length=255, help_text="JEE Main Rank")
    current_cgpa = models.CharField(max_length=255, help_text="Current CGPA")

    father_name = models.CharField(max_length=255, help_text="Father's Name")
    father_profession = models.CharField(
        max_length=255, help_text="Father's Profession"
    )
    father_contact_number = models.PositiveIntegerField(
        help_text="Father's Contact Number"
    )

    mother_name = models.CharField(max_length=255, help_text="Mother's Name")
    mother_profession = models.CharField(
        max_length=255, help_text="Mother's Profession"
    )

    mother_contact_number = models.PositiveIntegerField(
        help_text="Mother's Contact Number"
    )

    family_income_per_annum = models.CharField(
        max_length=255, help_text="Family income per annum"
    )

    bank_name = models.CharField(max_length=255, help_text="Student's Bank Name")
    bank_account_number = models.CharField(
        max_length=255, help_text="Bank Savings Account Number"
    )
    banK_address = models.CharField(max_length=255, help_text="Bank Branch Address")
    bank_ifsc_code = models.CharField(max_length=255, help_text="Bank IFSC Code")

    declaration = models.BooleanField(
        help_text="I acknowledge that I have read all the eligibility criteria of this scholarship and I am eligible "
                  "for applying to this scholarship."
    )

    status = models.CharField(
        max_length=1024,
        default="PENDING",
        choices=(
            ("PENDING", "PENDING"),
            ("APPROVED", "APPROVED"),
            ("REJECTED", "REJECTED"),
        ),
    )
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Application for [{self.scholarship.name[:15]}...]"

    class Meta:
        verbose_name_plural = "Merit cum Means Alumni Applications"
        verbose_name = "Merit cum Means Alumni Application"


class MCMOtherApplication(models.Model):
    """Scholarship Type: MCM_OTHER = 3"""

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)

    photograph = models.FileField(
        help_text="Passport size photograph in JPG/PNG under 2 MB.",
        blank=True,
        null=True,
        upload_to="photographs",
    )

    roll_no = models.CharField(max_length=20, help_text="Registration/Roll No")
    personal_contact_number = models.PositiveIntegerField()
    year = models.CharField(max_length=20, help_text="Year")
    branch = models.CharField(max_length=20, help_text="Branch")

    jee_main_rank = models.CharField(max_length=255, help_text="JEE Main Rank")
    current_cgpa = models.CharField(max_length=255, help_text="Current CGPA")

    father_name = models.CharField(max_length=255, help_text="Father's Name")
    father_profession = models.CharField(
        max_length=255, help_text="Father's Profession"
    )
    father_contact_number = models.PositiveIntegerField(
        help_text="Father's Contact Number"
    )

    mother_name = models.CharField(max_length=255, help_text="Mother's Name")
    mother_profession = models.CharField(
        max_length=255, help_text="Mother's Profession"
    )

    mother_contact_number = models.PositiveIntegerField(
        help_text="Mother's Contact Number"
    )

    family_income_per_annum = models.CharField(
        max_length=255, help_text="Family income per annum"
    )

    bank_name = models.CharField(max_length=255, help_text="Student's Bank Name")
    bank_account_number = models.CharField(
        max_length=255, help_text="Bank Savings Account Number"
    )
    banK_address = models.CharField(max_length=255, help_text="Bank Branch Address")
    bank_ifsc_code = models.CharField(max_length=255, help_text="Bank IFSC Code")

    declaration = models.BooleanField(
        help_text="I acknowledge that I have read all the eligibility criteria of this scholarship and I am eligible "
                  "for applying to this scholarship."
    )

    status = models.CharField(
        max_length=1024,
        default="PENDING",
        choices=(
            ("PENDING", "PENDING"),
            ("APPROVED", "APPROVED"),
            ("REJECTED", "REJECTED"),
        ),
    )
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Application for [{self.scholarship.name[:15]}...]"

    class Meta:
        verbose_name_plural = "Merit cum Means Other Applications"
        verbose_name = "Merit cum Means Other Application"


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
    category = models.ForeignKey(
        NoticeCategory, on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.TextField()
    attachment = models.FileField(blank=True, null=True, upload_to="notice_attachments")
    link = models.CharField(max_length=1024, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title


class Grievance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.TextField()
    issue_details = models.TextField()
    date_opened = models.DateTimeField(auto_now_add=True)

    resolved = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.subject


class ReceivedScholarship(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    year_of_study = models.CharField(max_length=1024, blank=True, null=True)
    branch = models.CharField(max_length=1024, default="UNSPECIFIED")
    programme = models.CharField(blank=True, null=True, max_length=1024)

    current_cgpa = models.FloatField(blank=True, null=True)
    cgpa_1st_semester = models.FloatField(blank=True, null=True)
    cgpa_2nd_semester = models.FloatField(blank=True, null=True)
    cgpa_3rd_semester = models.FloatField(blank=True, null=True)
    sgpa_5th_semester = models.FloatField(blank=True, null=True)
    sgpa_6th_semester = models.FloatField(blank=True, null=True)
    agpa = models.FloatField(blank=True, null=True)
    marks = models.FloatField(blank=True, null=True)
    jee_rank = models.FloatField(blank=True, null=True)
    pcme_percentage = models.FloatField(blank=True, null=True)
    pcb_percentage = models.FloatField(blank=True, null=True)
    ti_rank = models.FloatField(blank=True, null=True)
    tu_rank = models.FloatField(blank=True, null=True)
    twelfth_overall_percentage = models.FloatField(blank=True, null=True)

    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.scholarship.name


@dataclasses.dataclass
class ExcelError:
    row_id: int
    error_msg: str
