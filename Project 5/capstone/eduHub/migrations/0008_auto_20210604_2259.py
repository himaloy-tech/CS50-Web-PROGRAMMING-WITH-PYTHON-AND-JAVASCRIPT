# Generated by Django 3.1.5 on 2021-06-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduHub', '0007_auto_20210604_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
