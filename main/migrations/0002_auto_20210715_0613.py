# Generated by Django 3.2.5 on 2021-07-15 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='lat',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='details',
            name='long',
            field=models.CharField(default='', max_length=200),
        ),
    ]
