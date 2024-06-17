from django.db import models
from datetime import datetime

# Create your models here.
class Book(models.Model):
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)

    class Meta:
        db_table = "book_table"
        ordering = ['-pub_time', 'name']


class Author(models.Model):
    is_active = models.BooleanField()
    username = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    visit_count = models.IntegerField()
    # profile = models.CharField(max_length=200)
    profile = models.TextField()
    website = models.URLField()


class Tag(models.Model):
    name = models.CharField(max_length=200, db_column='tag_name', unique=True)
    create_time = models.DateTimeField(default=datetime.now)
    # 1. 可用，2：不可用
    # status = models.SmallIntegerField(default=1)



