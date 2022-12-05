# Generated by Django 4.1 on 2022-09-16 23:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_map', '0004_remove_log_post_log_type_alter_log_post_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stack',
            name='plant_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='calibration',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='log_post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]