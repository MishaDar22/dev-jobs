# Generated by Django 3.1.3 on 2020-12-06 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20201206_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to='MEDIA_SPECIALITY_IMAGE_DIR'),
        ),
    ]
