# Generated by Django 5.0.7 on 2024-07-18 09:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='file',
            field=models.FileField(blank=True, upload_to='musics', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])], verbose_name='File'),
        ),
    ]
