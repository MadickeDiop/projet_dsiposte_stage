# Generated by Django 2.1.4 on 2018-12-28 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=100)),
                ('equipement', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'configuration',
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='auteur',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
