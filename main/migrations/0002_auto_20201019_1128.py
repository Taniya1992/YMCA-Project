# Generated by Django 2.2 on 2020-10-19 05:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Profilel',
        ),
        migrations.RenameModel(
            old_name='Programs_category',
            new_name='Programs_categoryl',
        ),
        migrations.RenameModel(
            old_name='Programs',
            new_name='Programsl',
        ),
    ]