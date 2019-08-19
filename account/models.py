from django.db import models
from django.conf import settings

# Create your models here.
# user 如果登录的话是一个user对象，如果未登录，则是一个匿名用户
#用户注册和用户profiles

# 我们已经实现了如何login logout
# 还想像用户展现他们的 信息（profile）, 让他们注册
class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    date_of_birth = models.DateField()
    date_of_register = models.DateTimeField(auto_now_add=True)
    profile_photo = models.ImageField(upload_to=r'users/%Y/%m/%d', blank=True)
    # 在模板中，通过 {{ profile1.profile_photo.url }}
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

