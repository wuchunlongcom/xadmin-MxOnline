from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
import datetime

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

SERVER_STATUS = (
    (0, u"Normal"),
    (1, u"Down"),
    (2, u"No Connect"),
    (3, u"Error"),
)
SERVICE_TYPES = (
    ('moniter', u"Moniter"),
    ('lvs', u"LVS"),
    ('db', u"Database"),
    ('analysis', u"Analysis"),
    ('admin', u"Admin"),
    ('storge', u"Storge"),
    ('web', u"WEB"),
    ('email', u"Email"),
    ('mix', u"Mix"),
)


@python_2_unicode_compatible
class IDC(models.Model):
    name = models.CharField(max_length=64, verbose_name='IDC名称')
    description = models.TextField(verbose_name='描述')

    contact = models.CharField(max_length=32, verbose_name='联系人')
    telphone = models.CharField(max_length=32, verbose_name='电话')
    address = models.CharField(max_length=128, verbose_name='地址')
    customer_id = models.CharField(max_length=128, verbose_name='客户')
    groups = models.ManyToManyField(Group)  # many

    create_time = models.DateField(auto_now=True, verbose_name='创建日期')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"IDC 列表"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Host(models.Model):
    idc = models.ForeignKey(IDC, verbose_name='IDC', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name='Host名称')
    nagios_name = models.CharField(u"Nagios Host ID", max_length=64, blank=True, null=True)
    ip = models.GenericIPAddressField(verbose_name='ip',blank=True, null=True)
    internal_ip = models.GenericIPAddressField(verbose_name='内部ip', blank=True, null=True)
    user = models.CharField(verbose_name='用户', max_length=64)
    password = models.CharField(verbose_name='密码', max_length=128)
    ssh_port = models.IntegerField(verbose_name='ssh_port', blank=True, null=True)
    status = models.SmallIntegerField(verbose_name='状态', choices=SERVER_STATUS, default=SERVER_STATUS[0][0])

    brand = models.CharField(max_length=64, verbose_name='品牌', choices=[(i, i) for i in (u"DELL", u"HP", u"Other")])
    model = models.CharField(max_length=64, verbose_name='样式', choices=[(i, i) for i in (u"台式机", u"笔记本", u"其他")])
    cpu = models.CharField(max_length=64, verbose_name='CPU', choices=[(i, i) for i in (u"586", u"686")])
    core_num = models.SmallIntegerField(verbose_name='CoreNum', blank=True, null=True,choices=[(i * 2, "%s Cores" % (i * 2)) for i in range(1, 15)])
    hard_disk = models.IntegerField(verbose_name='硬盘', blank=True, null=True)
    memory = models.IntegerField(verbose_name='内存', blank=True, null=True)

    system = models.CharField(u"System OS", max_length=32, choices=[(i, i) for i in (u"CentOS", u"FreeBSD", u"Ubuntu")])
    system_version = models.CharField(max_length=32, choices=[(i, i) for i in (u"1.00", u"2.10", u"3.3.8")])
    system_arch = models.CharField(max_length=32, choices=[(i, i) for i in (u"x86_64", u"i386")])

    create_time = models.DateField(auto_now=True, verbose_name='创建日期')
    guarantee_date = models.DateField(auto_now=True,verbose_name='担保日期')
    service_type = models.CharField(max_length=32, verbose_name='服务类型', choices=SERVICE_TYPES, default=SERVICE_TYPES[0][0])
    description = models.TextField(verbose_name='描述')

    administrator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Admin")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Host 柱状图 表"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class MaintainLog(models.Model):
    """
        维护日志
    """
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    maintain_type = models.CharField(max_length=32, verbose_name='维护类型')
    hard_type = models.CharField(max_length=16, verbose_name='难度类型')
    time = models.DateTimeField(default=datetime.datetime.now)
    operator = models.CharField(max_length=16, verbose_name='操作人员')
    note = models.TextField(verbose_name='备注', default='备注:说点什么')

    def __str__(self):
        return '%s maintain-log [%s] %s %s' % (self.host.name, self.time.strftime('%Y-%m-%d %H:%M:%S'),
                                               self.maintain_type, self.hard_type)

    class Meta:
        verbose_name = "维护日志 列表" #"u"Maintain Log"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class HostGroup(models.Model):

    name = models.CharField(max_length=32, verbose_name='名称')
    description = models.TextField(verbose_name='描述')
    hosts = models.ManyToManyField(
        Host, verbose_name=u'Hosts', blank=True, related_name='groups')

    class Meta:
        verbose_name = u"Host Group 列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AccessRecord(models.Model):
    """
        访问记录
    """
    date = models.DateField(verbose_name='日期')
    user_count = models.IntegerField(verbose_name='用户数量')
    view_count = models.IntegerField(verbose_name='查看数量')

    class Meta:
        verbose_name = "访问记录 图表" # u"Access Record"
        verbose_name_plural = verbose_name

    def __str__(self):
        #return "%s 访问记录" % self.date.strftime('%Y-%m-%d')
        return "%s Access Record" % self.date.strftime('%Y-%m-%d')

#add
class School(models.Model):
 
    name = models.CharField(max_length=50,verbose_name='学校名字')
    address = models.CharField(max_length=100,verbose_name='学校地址')
    date = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True,verbose_name='添加时间')
    num = models.IntegerField(verbose_name='建校时间', blank=True, null=True)
    
    class Meta:
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Threshold(models.Model):

    num = models.IntegerField(verbose_name='阀值', default=20)
    
    class Meta:
        verbose_name='阀值'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.num   
    
    
    
    
class Test(models.Model):
    
    class Meta:
        verbose_name = u"自定义页面"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Meta.verbose_name

