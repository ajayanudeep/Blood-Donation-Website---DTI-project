# Generated by Django 3.2.5 on 2021-07-26 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(default='', max_length=200)),
                ('long', models.CharField(default='', max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(default='male', max_length=6)),
                ('blood_type', models.CharField(max_length=3)),
                ('mobile', models.BigIntegerField()),
                ('hospital', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
