# Generated by Django 2.1.4 on 2019-01-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190104_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='equipement',
            field=models.FileField(blank=True, null=True, upload_to='equipements'),
        ),
    ]