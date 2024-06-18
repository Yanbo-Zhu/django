# Generated by Django 5.0.3 on 2024-03-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('username', models.CharField(max_length=200)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('visit_count', models.IntegerField()),
                ('profile', models.TextField()),
                ('website', models.URLField()),
            ],
        ),
    ]