# Generated by Django 3.0.2 on 2020-05-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCPapp', '0011_auto_20200511_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='id',
        ),
        migrations.AlterField(
            model_name='login',
            name='rollNumber',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
