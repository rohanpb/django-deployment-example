# Generated by Django 5.0.2 on 2024-02-29 08:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("first_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="accessrecord",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
