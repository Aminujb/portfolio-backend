# Generated by Django 3.1.1 on 2021-01-06 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_remove_template_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='template',
            new_name='name',
        ),
    ]
