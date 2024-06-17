# Generated by Django 5.0.3 on 2024-03-31 02:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(db_column='tag_name', max_length=200, unique=True),
        ),
    ]
