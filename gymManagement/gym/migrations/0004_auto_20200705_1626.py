# Generated by Django 3.0.7 on 2020-07-05 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_auto_20200705_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='initalammount',
            new_name='initial',
        ),
    ]