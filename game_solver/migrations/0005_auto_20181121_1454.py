# Generated by Django 2.1.3 on 2018-11-21 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_solver', '0004_remove_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date created'),
        ),
    ]
