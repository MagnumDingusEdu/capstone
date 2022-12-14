# Generated by Django 4.1.3 on 2022-12-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_session_remove_student_cat_type_and_more"),
        ("website", "0012_notice_link_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MCMApplication",
            new_name="MCMTietApplication",
        ),
        migrations.AlterField(
            model_name="scholarship",
            name="scholarship_type",
            field=models.IntegerField(
                choices=[
                    (1, "Mcm Tiet"),
                    (2, "Mcm Alumni"),
                    (3, "Mcm Other"),
                    (4, "Merit Alumni"),
                    (5, "Merit Auto"),
                ]
            ),
        ),
    ]
