# Generated by Django 3.0.5 on 2020-05-14 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_rejister_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rejister',
            name='desc',
        ),
    ]