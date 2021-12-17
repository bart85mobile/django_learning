# Generated by Django 3.2.5 on 2021-12-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_contracts', '0002_rename_distinct_businessentity_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessentity',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='businessentity',
            name='address2',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='businessentity',
            name='postcode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='businessentity',
            name='region',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
