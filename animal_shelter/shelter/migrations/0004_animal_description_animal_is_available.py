# Generated by Django 5.1.2 on 2024-10-22 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0003_animal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
