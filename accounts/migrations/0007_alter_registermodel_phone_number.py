# Generated by Django 4.2.5 on 2023-09-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_registermodel_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
