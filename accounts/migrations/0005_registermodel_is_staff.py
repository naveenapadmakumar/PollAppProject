# Generated by Django 4.2.5 on 2023-09-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_registermodel_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='registermodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
