# Generated by Django 5.1 on 2024-09-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='identification_number',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]