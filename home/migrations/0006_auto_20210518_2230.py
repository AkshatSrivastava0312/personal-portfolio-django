# Generated by Django 3.2 on 2021-05-18 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210517_0646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagegallery',
            options={'verbose_name_plural': 'Image Gallery'},
        ),
        migrations.AlterModelOptions(
            name='topskills',
            options={'verbose_name_plural': 'Top Skills'},
        ),
    ]
