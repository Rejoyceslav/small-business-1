# Generated by Django 3.2.8 on 2021-11-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_materialy_dupa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialy',
            name='dupa',
        ),
        migrations.AddField(
            model_name='materialy',
            name='description2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='materialy',
            name='description3',
            field=models.TextField(blank=True, null=True),
        ),
    ]