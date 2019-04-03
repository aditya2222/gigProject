# Generated by Django 2.1.7 on 2019-04-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190403_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indexTitle', models.CharField(blank=True, max_length=120, null=True)),
                ('indexBodyHeader', models.CharField(blank=True, max_length=120, null=True)),
                ('indexBodySubHeader', models.CharField(blank=True, max_length=120, null=True)),
                ('idnexLeftHeader', models.CharField(blank=True, max_length=120, null=True)),
                ('indexLeftHeaderContent', models.CharField(blank=True, max_length=120, null=True)),
                ('indexFeatured', models.CharField(blank=True, max_length=120, null=True)),
                ('directLinkText1', models.CharField(blank=True, max_length=120, null=True)),
                ('directLinkText2', models.CharField(blank=True, max_length=120, null=True)),
                ('directLinkText3', models.CharField(blank=True, max_length=120, null=True)),
                ('directLinkText4', models.CharField(blank=True, max_length=120, null=True)),
                ('directLinkText5', models.CharField(blank=True, max_length=120, null=True)),
                ('directLinkText6', models.CharField(blank=True, max_length=120, null=True)),
                ('directLinkText7', models.CharField(blank=True, max_length=120, null=True)),
                ('directLinkText8', models.CharField(blank=True, max_length=120, null=True)),
                ('FooterTitle', models.CharField(blank=True, max_length=120, null=True)),
                ('FooterTitle2', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='mainHeader',
            new_name='Link1Text',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='subHeader',
            new_name='Link2Text',
        ),
        migrations.RenameField(
            model_name='pagesmodel',
            old_name='title',
            new_name='Link3Text',
        ),
        migrations.RemoveField(
            model_name='pagesmodel',
            name='About',
        ),
        migrations.RemoveField(
            model_name='pagesmodel',
            name='Footer',
        ),
        migrations.RemoveField(
            model_name='pagesmodel',
            name='Image1',
        ),
        migrations.RemoveField(
            model_name='pagesmodel',
            name='Image2',
        ),
        migrations.RemoveField(
            model_name='pagesmodel',
            name='Image3',
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='Link4Text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='Link5Text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='Link6Text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='Link7Text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='Link8Text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='footerTitle',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='footerTitle2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='h2more',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='h2name2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='headerTitle',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='headingName1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='pagesmodel',
            name='p1Middle',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]