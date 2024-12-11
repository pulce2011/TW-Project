# Generated by Django 5.1.3 on 2024-12-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dettagli',
            name='memoria',
            field=models.PositiveIntegerField(choices=[(64, '64 GB'), (128, '128 GB'), (256, '256 GB'), (512, '512 GB'), (1024, '1 TB')], default=64),
        ),
    ]