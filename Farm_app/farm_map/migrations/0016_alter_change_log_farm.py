# Generated by Django 4.1 on 2022-11-03 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_map', '0015_alter_change_log_suggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='change_log',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm', to='farm_map.farm_location'),
        ),
    ]
