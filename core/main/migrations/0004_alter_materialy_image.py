# Generated by Django 3.2.8 on 2021-11-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211124_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='materialy_images/'),
        ),
    ]
