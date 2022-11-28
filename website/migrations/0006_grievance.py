# Generated by Django 4.1.3 on 2022-11-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_mcmapplication_remarks_mcmapplication_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Grievance",
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
                ("subject", models.TextField()),
                ("issue_details", models.TextField()),
                ("date_opened", models.DateTimeField(auto_now_add=True)),
                ("resolved", models.BooleanField(default=False)),
            ],
        ),
    ]
