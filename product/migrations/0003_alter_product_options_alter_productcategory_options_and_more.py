# Generated by Django 5.1 on 2024-10-07 12:57

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_unitofmeasure_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product Category'},
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='product.productcategory', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_type_for_sped',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.itemtypeforsped', verbose_name='Item Type For SPED'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price Cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku_code',
            field=models.CharField(max_length=20, unique=True, verbose_name='Code (SKU)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_of_measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.unitofmeasure', verbose_name='Unit Of Measure'),
        ),
    ]