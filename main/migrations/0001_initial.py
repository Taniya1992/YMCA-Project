# Generated by Django 2.2 on 2020-10-19 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Programs_category_name', models.CharField(max_length=1000)),
                ('Program_name', models.CharField(max_length=1000)),
                ('Price_for_ymca_Member', models.CharField(max_length=1000)),
                ('Price_for_non_ymca_Member', models.CharField(max_length=1000)),
                ('StartingDate', models.DateField(max_length=1000)),
                ('EndingDate', models.DateField(max_length=1000)),
                ('StartingTime', models.TimeField()),
                ('EndingTime', models.TimeField()),
                ('Location', models.TextField(max_length=1000)),
                ('Description', models.TextField(max_length=1000)),
                ('Participant_allowed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Programs_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Program_category_name', models.CharField(max_length=1000)),
                ('Program_Description', models.CharField(max_length=10000)),
                ('Program_logo', models.FileField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username1', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Gender', models.CharField(blank=True, max_length=100)),
                ('Contact_Number', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('Address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
