# Generated by Django 3.1.3 on 2020-11-09 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201108_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='goal',
        ),
    ]
