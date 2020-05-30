# Generated by Django 3.0.5 on 2020-05-14 21:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_remove_rejister_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='rejister',
            name='cources',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rejister',
            name='gender',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
