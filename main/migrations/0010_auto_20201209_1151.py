# Generated by Django 2.2 on 2020-12-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_programs_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Cancel', 'Cancel')], default='Active', max_length=100),
        ),
        migrations.AlterField(
            model_name='programs',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Cancel', 'Cancel')], default='Active', max_length=100),
        ),
    ]
