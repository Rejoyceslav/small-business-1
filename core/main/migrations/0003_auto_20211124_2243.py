# Generated by Django 3.2.8 on 2021-11-24 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_alter_materialy_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialy',
            name='image',
            field=models.ImageField(blank=True, upload_to='materialy_images'),
        ),
        migrations.AddField(
            model_name='materialy',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='materialy',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
