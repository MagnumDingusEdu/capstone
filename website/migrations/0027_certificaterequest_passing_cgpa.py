# Generated by Django 4.1.3 on 2022-12-05 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0026_alter_certificaterequest_date_approved_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificaterequest",
            name="passing_cgpa",
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
