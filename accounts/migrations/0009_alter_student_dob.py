# Generated by Django 4.1.3 on 2022-12-05 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0008_remove_student_current_session_alter_student_app_no_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="dob",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]