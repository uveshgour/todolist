# Generated by Django 4.0.4 on 2022-06-15 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Descriptions',
            new_name='Description_Box',
        ),
    ]
