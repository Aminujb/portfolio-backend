# Generated by Django 3.1.1 on 2021-01-06 08:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210105_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.CharField(max_length=20)),
                ('rating', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, max_length=1)),
                ('submitted_by', models.CharField(max_length=80)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2021, 1, 6, 9, 43, 49, 487961))),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.template'),
        ),
    ]
