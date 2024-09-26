# Generated by Django 5.1 on 2024-09-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0009_vacation_unique_employee_hiring_start_and_end_date'),
        ('product', '0001_initial'),
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brand'},
        ),
        migrations.AlterModelOptions(
            name='toolcategory',
            options={'verbose_name': 'Tool Category'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='tool_status',
            field=models.CharField(choices=[('new', 'New'), ('lightly_used', 'Lightly Used'), ('used', 'Used'), ('worn', 'Worn'), ('broken', 'Broken'), ('under_repair', 'Under Repair'), ('discarded', 'Discarded')], default='new', max_length=12, verbose_name='Tool Status'),
        ),
        migrations.AlterField(
            model_name='toolcategory',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AddConstraint(
            model_name='tool',
            constraint=models.UniqueConstraint(fields=('item', 'asset_number'), name='unique_item_asset_number'),
        ),
        migrations.AddConstraint(
            model_name='tooldistributionrecord',
            constraint=models.UniqueConstraint(fields=('tool', 'employee'), name='unique_tool_employee'),
        ),
    ]
