# Generated by Django 3.0.7 on 2020-11-25 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201113_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails'),
        ),
    ]
