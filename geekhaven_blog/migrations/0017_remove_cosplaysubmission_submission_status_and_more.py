# Generated by Django 4.2.10 on 2024-03-30 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geekhaven_blog", "0016_cosplaysubmission_approval_state"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cosplaysubmission",
            name="submission_status",
        ),
        migrations.DeleteModel(
            name="BlogComment",
        ),
    ]
