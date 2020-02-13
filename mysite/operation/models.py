# operation/models.py

from datetime import datetime

from django.db import models

from course.models import Course
from users.models import UserProfile


class UserAsk(models.Model):
    '''用户咨询 （对应首页我要学习）'''
    name = models.CharField('姓名',max_length=20)
    mobile = models.CharField('手机',max_length=11)
    course_name = models.CharField('课程名',max_length=50)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseComments(models.Model):
    '''课程评论 （对应首页 公开课开始学习 评论）'''
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    comments = models.CharField('评论',max_length=200,  default='教学效果好，值得推广')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    '''用户收藏 （对应首页 公开课开始学习 收藏）'''
    FAV_TYPE = (
        (1,'课程'),
        (2,'课程机构'),
        (3,'讲师')
    )

    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    fav_id = models.IntegerField('数据id',default=0)  # 默认不收藏
    fav_type = models.IntegerField(verbose_name='收藏类型',choices=FAV_TYPE,default=1)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField('接受用户',default=0) # 默认不接受用户
    message = models.CharField('消息内容',max_length=500)
    has_read = models.BooleanField('是否已读',default=False)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    '''用户课程'''
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
