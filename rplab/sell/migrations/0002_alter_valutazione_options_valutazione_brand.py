# Generated by Django 5.1.3 on 2024-12-10 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valutazione',
            options={'verbose_name_plural': 'Valutazioni'},
        ),
        migrations.AddField(
            model_name='valutazione',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.brand'),
        ),
    ]