# Generated by Django 4.1 on 2023-01-13 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_map', '0021_alter_produce_harvest_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produce', to='farm_map.farm_location'),
        ),
    ]
