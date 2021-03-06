# Generated by Django 2.1.7 on 2019-04-07 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190403_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexmodel',
            old_name='FooterTitle',
            new_name='bannerImage',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='FooterTitle2',
            new_name='indexBannerText',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='directLinkText1',
            new_name='indexBannerText2',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='directLinkText2',
            new_name='indexFeaturedImage',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='directLinkText3',
            new_name='indexFeaturedLink',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='directLinkText4',
            new_name='indexFeaturedP',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='directLinkText5',
            new_name='indexHeaderTitle',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='directLinkText6',
            new_name='indirectLink1',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='directLinkText7',
            new_name='indirectLink2',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='directLinkText8',
            new_name='indirectLink3',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='idnexLeftHeader',
            new_name='indirectLink4',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='indexBodyHeader',
            new_name='indirectLink5',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='indexBodySubHeader',
            new_name='indirectLink6',
        ),
        migrations.RenameField(
            model_name='indexmodel',
            old_name='indexLeftHeaderContent',
            new_name='indirectLink7',
        ),
        migrations.AlterField(
            model_name='indexmodel',
            name='indexTitle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
