# Generated by Django 2.2.8 on 2020-09-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200828_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('first_name',), 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(default='', max_length=50, verbose_name='Job Title'),
        ),
    ]
