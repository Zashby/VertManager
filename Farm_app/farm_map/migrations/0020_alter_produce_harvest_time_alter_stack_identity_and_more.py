# Generated by Django 4.1 on 2023-01-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_map', '0019_species_change_log_down_votes_change_log_immolate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produce',
            name='harvest_time',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='stack',
            name='identity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='zone',
            name='identity',
            field=models.PositiveIntegerField(),
        ),
    ]