# Generated by Django 3.0.6 on 2020-05-22 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SCPapp', '0016_remove_file_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentsexp',
            name='created',
        ),
        migrations.RemoveField(
            model_name='commentspyq',
            name='created',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='created',
        ),
    ]
