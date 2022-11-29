# Generated by Django 4.1.3 on 2022-11-28 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0003_student_adm_mode_student_app_no_student_branch_code_and_more",
        ),
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MCMApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contact_number", models.PositiveIntegerField()),
                ("alternate_contact_number", models.PositiveIntegerField()),
                (
                    "state_of_residence",
                    models.CharField(
                        choices=[
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
                            (
                                "Andaman and Nicobar Islands",
                                "Andaman and Nicobar Islands",
                            ),
                            ("Chandigarh", "Chandigarh"),
                            (
                                "Dadra and Nagar Haveli and Daman & Diu",
                                "Dadra and Nagar Haveli and Daman & Diu",
                            ),
                            (
                                "The Government of NCT of Delhi",
                                "The Government of NCT of Delhi",
                            ),
                            ("Jammu & Kashmir", "Jammu & Kashmir"),
                            ("Ladakh", "Ladakh"),
                            ("Lakshadweep", "Lakshadweep"),
                            ("Puducherry", "Puducherry"),
                        ],
                        max_length=255,
                    ),
                ),
                ("class_12_marks", models.CharField(max_length=255)),
                (
                    "current_cgpa_or_rank",
                    models.CharField(
                        help_text="Current CGPA or Rank or Diploma %", max_length=255
                    ),
                ),
                (
                    "family_income_per_mcm_application",
                    models.CharField(
                        help_text="FAMILY INCOME AS MENTIONED IN MCM APPLICATION FORM",
                        max_length=255,
                    ),
                ),
                (
                    "family_income_per_affidavit",
                    models.CharField(
                        help_text="FAMILY INCOME AS PER AFFIDAVIT ATTACHED",
                        max_length=255,
                    ),
                ),
                (
                    "family_income_per_certificate",
                    models.CharField(
                        help_text="FAMILY INCOME AS PER CERTIFICATE OF TEHSILDAR",
                        max_length=255,
                    ),
                ),
                ("bank_balance", models.IntegerField()),
                ("fdr_balance", models.CharField(max_length=255)),
                (
                    "itr_annual_year_current",
                    models.IntegerField(help_text="ITR for this annual year"),
                ),
                (
                    "itr_annual_year_last",
                    models.IntegerField(help_text="ITR for previous annual year"),
                ),
                (
                    "itr_annual_year_last_last",
                    models.IntegerField(help_text="ITR for last to last annual year"),
                ),
                (
                    "immovable_property",
                    models.BooleanField(
                        help_text="IMMOVABLE PROPERTY AS PER AFFIDAVIT"
                    ),
                ),
                (
                    "single_girl_child",
                    models.BooleanField(help_text="Are you a Single Girl Child?"),
                ),
                (
                    "applied_for_mcp_special",
                    models.BooleanField(help_text="APPLIED FOR MCM SPECIAL?"),
                ),
                (
                    "mcp_special_reason",
                    models.TextField(
                        help_text="SPECIFIC REASON FOR APPLYING MCM SPECIAL?"
                    ),
                ),
                (
                    "applied_for_other_scholarship",
                    models.BooleanField(
                        help_text="HAVE YOU APPLIED FOR ANY OTHER SCHOLARSHIP?"
                    ),
                ),
                (
                    "other_scholarship_details",
                    models.TextField(help_text="DETAILS OF OTHER SCHOLARSHIP APPLIED"),
                ),
                (
                    "previous_year_scholarship",
                    models.BooleanField(
                        help_text="HAVE YOU RECEIVED ANY SCHOLARSHIP IN THE PREVIOUS YEAR?"
                    ),
                ),
                (
                    "previous_year_scholarship_details",
                    models.TextField(
                        help_text="DETAILS OF PREVIOUS SCHOLARSHIP RECEIVED"
                    ),
                ),
                (
                    "previous_year_scholarship_amount",
                    models.IntegerField(help_text="AMOUNT OF THE PREVIOUS SCHOLARSHIP"),
                ),
                (
                    "declaration",
                    models.BooleanField(
                        help_text="I acknowledge that i have read all the eligibility criteria of scholarship and i am eligible for applying to TIET Merit-cum-means scholarship."
                    ),
                ),
                (
                    "scholarship",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="website.scholarship",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.student",
                    ),
                ),
            ],
            options={
                "verbose_name": "Merit cum means Application",
                "verbose_name_plural": "Merit cum Means Applications",
            },
        ),
        migrations.AlterModelOptions(
            name="scholarshipcategory",
            options={"verbose_name_plural": "Scholarship Categories"},
        ),
        migrations.DeleteModel(
            name="MCMApp",
        ),
    ]