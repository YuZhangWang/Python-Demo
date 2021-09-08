from django.db import models


class userdata(models.Model):
    username = models.CharField(max_length=128, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱', unique=True)
    ip = models.CharField(max_length=128, verbose_name='IP地址')
