# Generated by Django 3.2.13 on 2022-06-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=10)),
                ('Descriptions', models.CharField(max_length=500)),
                ('Date', models.DateField()),
                ('Complete', models.BooleanField()),
            ],
        ),
    ]
