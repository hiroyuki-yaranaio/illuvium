# Generated by Django 4.1.4 on 2023-01-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_people_registrationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='Password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
