# Generated by Django 4.1.2 on 2022-10-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]