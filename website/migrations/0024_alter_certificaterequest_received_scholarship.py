# Generated by Django 4.1.3 on 2022-12-05 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0023_certificaterequest_date_approved_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificaterequest",
            name="received_scholarship",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="website.receivedscholarship",
            ),
        ),
    ]
