# -*- coding: UTF-8 -*-
import os
import sys
import  django
import random

if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    
    from django.contrib.auth.models import User, Group, Permission 
    from app.models import AccessRecord, IDC, Host, SERVICE_TYPES, HostGroup, MaintainLog
    from basedao import BaseDAO
    

    items = [{'date':'2020-01-01','user_count':'10','view_count':'30'},\
             {'date':'2020-03-01','user_count':'100','view_count':'500'},\
             {'date':'2020-05-01','user_count':'15','view_count':'300'},\
             {'date':'2020-07-01','user_count':'80','view_count':'160'},]
    BaseDAO(AccessRecord).save_batch(items)
    
    names = ['张权', '李伟中', '赵有原','崔力文', '许东方', '钱宝才', '孙悟空']
    
    IDC_NUM = 20
    idcGroup = Group.objects.create(name='IDCGroup')
    idcGroup.save()
    for i in range(IDC_NUM):
        idc = IDC()
        idc.name = 'IDC名称-%s' % i
        idc.description = '描述-%s' % i
        idc.contact = random.choice(names)
        idc.telphone = '138' + ''.join([str(random.randint(0,9)) for _i in range(8)])
        idc.address = '北京中关村%s号' % random.randint(1, 2000)
        idc.customer_id = random.choice(['中国银行', '中国工商银行', '中国农业银行',
                                    '中国建设银行', '中国交通银行', '招商银行', '民生银行'])
        #idc.groups.add(1)  # many 多对多 这样赋值是不行的！       
        idc.save()
        
        # many 多对多 这样赋值
        idc = IDC.objects.get(id = i+1)
        idc.groups.add(1)  # many     
        idc.save()

    HOST_NUM = 10
    for i in range(HOST_NUM):
        h = Host()
        h.idc = IDC.objects.get(id = i+1)
        h.name = 'Host名称-%s' % i
        h.user = random.choice(names)
        h.password = '123'
        h.memory = random.choice([4,8,16]) 
        h.service_type = SERVICE_TYPES[random.randint(0,8)][0]
        h.description = '描述 --' + ''.join([str(random.randint(0,9)) for _i in range(8)])   
        h.administrator = User.objects.get(id=i+1)        
        h.save()

    HOST_NUM = 10
    for i in range(HOST_NUM):
        h = HostGroup()
        h.name = 'Host名称-%s' % i
        h.description = '描述 --' + ''.join([str(random.randint(0,9)) for _i in range(8)])
        h.save()
        
        # many 多对多 这样赋值
        h = HostGroup.objects.get(id = i+1)
        h.hosts.add(2,4,6,8) if i%2 else h.hosts.add(1,3,5,7,9)   # many    
        h.save()
    
    MAINTAIN_NUM = 10
    for i in range(MAINTAIN_NUM):
        m = MaintainLog()
        m.host = Host.objects.get(id = random.randint(1,9))
        m.maintain_type = random.choice(['硬件维护','软件维护'])
        m.hard_type = random.choice(['简单','复杂','非常复杂'])
        m.operator = random.choice(names)
        m.save()
        
    #BaseDAO(School).delete({}) #删除全部记录    
    #BaseDAO(School).delete_batch([{'id':1},{'id':2}]) #删除仅保留ID=1 ID=2记录
    #BaseDAO(School).delete_batch_exclude({},{'id':2}) #删除仅保留ID=2的全部记录
    #terms = [({'name':'清华大学'},{'address':'中国北京'}),({'name':'复旦大学'},{'address':'中国上海'})]
    #BaseDAO(School).update_batch(terms)
    #BaseDAO(School).update_batch_exclude({},{},{'name':'大学','address':'中国'}) #将全部记录'name'更新为'大学'，'address'更新为'中国'                                                                    
    #print(BaseDAO(School).all()) 
    #print(BaseDAO(School).filter_exclude({'name':'北京大学'},{'address':'北京'}))                                                                     
                                                                         
                                                                         