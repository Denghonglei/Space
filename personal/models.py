from django.db import models

# Create your models here.
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):  # 类别模型

    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'Category'


class UserProfile(AbstractUser):  # AUTH_USER_MODEL = 'users.UserProfile' #重载settings的方法

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        db_table = 'UserProfile'

    def __unicode__(self):
        return self.name


class VerifyCode(models.Model):  # 短信验证码
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name
        db_table = 'VerifyCode'

    def __unicode__(self):
        return self.code


class Goods(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField(max_length=255,blank=True,null=True,verbose_name='标题')
    detail =  models.CharField(max_length=255,blank=True,null=True,verbose_name='详情介绍')
    pic_index  = models.TextField(null=True, blank=True,verbose_name='标题图')
    nine_pics = models.TextField(null=True, blank=True,verbose_name='九宫格')
    all_pics = models.TextField(null=True, blank=True,verbose_name='所有图')
    is_delete = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    praise_count = models.IntegerField(default=1,verbose_name='点赞数')
    browse_count = models.IntegerField(default=1,verbose_name='浏览量')
    create_time = models.DateTimeField(auto_now_add=True)
    type_one = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Goods"

