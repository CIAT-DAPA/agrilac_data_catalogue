# Generated by Django 5.0.7 on 2024-08-05 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Visitor', 'Visitor')], default='Visitor', max_length=10),
        ),
    ]
