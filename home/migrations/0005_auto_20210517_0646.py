# Generated by Django 3.2 on 2021-05-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_imagegallery_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallery',
            name='imageUrl',
            field=models.ImageField(default='', upload_to='home/gallery'),
        ),
        migrations.AlterField(
            model_name='tagline',
            name='text',
            field=models.TextField(max_length=250),
        ),
    ]
