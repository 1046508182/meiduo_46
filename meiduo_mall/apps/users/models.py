from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 自定义用户模型类    （个人理解）因为父类中没有手机号
    mobile = models.CharField(max_length=11,unique=True,verbose_name='手机号')
    class Meta:
        db_table = "tb_users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        # username是返回的父类中的username（个人理解）
        return self.username
