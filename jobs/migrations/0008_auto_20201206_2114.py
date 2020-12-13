# Generated by Django 3.1.3 on 2020-12-06 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0007_company_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(height_field=100, upload_to='MEDIA_COMPANY_IMAGE_DIR', width_field=60),
        ),
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(height_field=80, upload_to='MEDIA_SPECIALITY_IMAGE_DIR', width_field=80),
        ),
    ]