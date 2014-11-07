#coding=utf-8
from django.db import models
from django.contrib import admin
# Create your models here.
# 数据库中model的字段
class User(models.Model):
    username=models.CharField(max_length=50) #用户名
    password= models.CharField(max_length=50) #密码
    def __unicode__(self): # 字段格式化成字符串格式
        return self.username
class UserAdmin(admin.ModelAdmin):
    list_display = ("username","password")
admin.site.register(User)
