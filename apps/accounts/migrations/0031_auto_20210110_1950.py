# Generated by Django 3.1.1 on 2021-01-10 19:50

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_contact_created_on'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='resume',
            new_name='template',
        ),
    ]
