# Generated by Django 2.1.7 on 2019-04-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190407_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexmodel',
            name='indexLeftHeader',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='indexmodel',
            name='indexLeftHeaderContent',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
