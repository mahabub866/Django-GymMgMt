# Generated by Django 3.0.7 on 2020-07-05 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20200705_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='initialammount',
            new_name='initalammount',
        ),
    ]
