# Generated by Django 3.1.12 on 2021-06-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210630_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]