# Generated by Django 4.2.10 on 2024-03-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geekhaven_blog", "0014_useraccount_cosplaysubmission"),
    ]

    operations = [
        migrations.AddField(
            model_name="cosplaysubmission",
            name="submission_status",
            field=models.IntegerField(
                choices=[(0, "Draft"), (1, "Published")], default=0
            ),
        ),
    ]
