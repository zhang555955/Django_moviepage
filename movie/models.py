# coding=utf-8
from __future__ import unicode_literals
from django.db import models


# Create your models here.

# 页码 num 每页显示记录数 size
#       1      2   [0:2]
#       2      2   [2:4]
#       3      2   [4:6]
#       num    size [((num-1)*size):(num*size)]

class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(unique=True, max_length=100)
    mdesc = models.TextField(blank=True, null=True)
    ming = models.CharField(max_length=120)
    mlink = models.CharField(max_length=200)

    # class Meta:
    #     managed = False
    #     db_table = 'movie'


# if __name__ == "__main__":
#     Movie().contributable_attrs()