# Generated by Django 2.1.7 on 2019-04-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190407_0458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='Link1Text',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='Link2Text',
            new_name='footerLink',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='Link3Text',
            new_name='footerLinkText',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='Link4Text',
            new_name='footerp1',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='Link5Text',
            new_name='h2name1',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='Link6Text',
            new_name='h4name',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='Link7Text',
            new_name='keywords',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='Link8Text',
            new_name='link1',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='headerTitle',
            new_name='link1text',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='headingName1',
            new_name='link2',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='p1Middle',
            new_name='link2text',
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link3text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link4',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link4text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link5',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link5text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link6',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link6text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link7',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link7text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link8',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='link8text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='logoalt',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='logolink',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='logopath',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='p1middle',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='p2middle',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='primaryLink',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
