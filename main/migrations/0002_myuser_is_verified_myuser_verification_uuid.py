# Generated by Django 4.1.7 on 2023-07-21 11:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="myuser",
            name="is_verified",
            field=models.BooleanField(default=False, verbose_name="verified"),
        ),
        migrations.AddField(
            model_name="myuser",
            name="verification_uuid",
            field=models.UUIDField(
                default=uuid.uuid4, verbose_name="Unique Verification UUID"
            ),
        ),
    ]