# Generated by Django 2.1.7 on 2019-04-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190407_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagesmodel',
            name='logopath',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
