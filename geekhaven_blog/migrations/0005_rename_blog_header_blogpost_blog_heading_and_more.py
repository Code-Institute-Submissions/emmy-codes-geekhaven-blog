# Generated by Django 4.2.10 on 2024-03-04 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geekhaven_blog', '0004_blogpost_blog_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='blog_header',
            new_name='blog_heading',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='header_image',
            new_name='heading_image',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='slug',
            new_name='url_slug',
        ),
    ]
