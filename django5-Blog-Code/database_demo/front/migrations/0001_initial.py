# Generated by Django 5.0.3 on 2024-04-01 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'front_author',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'front_publisher',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('pages', models.IntegerField()),
                ('price', models.FloatField()),
                ('rating', models.FloatField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.publisher')),
            ],
            options={
                'db_table': 'front_book',
            },
        ),
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.book')),
            ],
            options={
                'db_table': 'front_book_order',
            },
        ),
    ]