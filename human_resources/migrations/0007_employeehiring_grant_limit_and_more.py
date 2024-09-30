# Generated by Django 5.1 on 2024-09-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0006_alter_employee_pis_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeehiring',
            name='grant_limit',
            field=models.DateField(blank=True, null=True, verbose_name='Grant Limit'),
        ),
        migrations.AddField(
            model_name='employeehiring',
            name='vacation_expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Vacation Expiration Date'),
        ),
    ]