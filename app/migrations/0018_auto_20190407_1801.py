# Generated by Django 2.1.7 on 2019-04-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20190407_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexmodel',
            name='indirectLink8',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='indexmodel',
            name='indirectLink8text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
