# Generated by Django 3.1.1 on 2021-01-06 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20210106_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
