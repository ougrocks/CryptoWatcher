# Generated by Django 2.0.1 on 2018-01-14 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='btc',
            old_name='date',
            new_name='date_b',
        ),
    ]
