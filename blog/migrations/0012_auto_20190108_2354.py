# Generated by Django 2.1.4 on 2019-01-08 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190108_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configuration',
            options={},
        ),
        migrations.AlterField(
            model_name='configuration',
            name='equipement',
            field=models.ImageField(blank=True, null=True, upload_to='equipement'),
        ),
    ]
