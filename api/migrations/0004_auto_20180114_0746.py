# Generated by Django 2.0.1 on 2018-01-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180114_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btc',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]
