# Generated by Django 3.1.1 on 2021-01-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20210106_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='', help_text='Professional Summary', max_length=500, null=True),
        ),
    ]
