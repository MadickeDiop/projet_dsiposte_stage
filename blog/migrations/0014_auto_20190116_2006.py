# Generated by Django 2.1.4 on 2019-01-16 20:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20190111_0054'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Configuration',
            new_name='Superviser',
        ),
    ]
