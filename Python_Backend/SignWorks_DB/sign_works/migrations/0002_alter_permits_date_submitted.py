# Generated by Django 3.2 on 2024-02-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_works', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permits',
            name='date_submitted',
            field=models.DateField(blank=True, null=True),
        ),
    ]
