# Generated by Django 4.1 on 2023-01-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_map', '0020_alter_produce_harvest_time_alter_stack_identity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produce',
            name='harvest_time',
            field=models.PositiveIntegerField(default=28),
        ),
    ]
