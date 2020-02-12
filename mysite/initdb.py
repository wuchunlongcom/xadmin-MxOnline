# -*- coding: UTF-8 -*-
import os
import sys
import  django
print('python 版本: %s。\ndjango版本: %s。'%(sys.version, django.get_version()))

if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    
    import random
    from users.models import UserProfile
         
    # 用户名与邮箱是关联的，因此邮箱不能重复
    UserProfile.objects.create_superuser('admin','wcl6005@126.com','admin')  # 超级用户
    UserProfile.objects.create_superuser('root','root@126.com','admin')  # 超级用户  
    UserProfile.objects.create_user('wcl6005','wcl@126.com','admin')  # 普通用户
    
    from basedao import BaseDAO 
      
    from organization.models import CityDict, CourseOrg, Teacher    
    terms = {'name':'北京','desc':'北京市，简称“京”，是中华人民共和国首都、也是中国4个直辖市之一'}
    BaseDAO(CityDict).save(terms) 
    items = [{'name':'上海','desc':'上海市，简称沪，是中国4个直辖市之一，是中国经济、金融、贸易、航运、科技创新中心。'}, {'name':'广州','desc':'广州是国家历史文化名城，从秦朝开始一直是郡治、州治、府治的所在地，华南地区的政治、军事、经济、文化和科教中心'}]
    BaseDAO(CityDict).save_batch(items)
    
    address = [(1,'中关村新安路38号'),(2,'闸北区幸福路1039号'),(3,'科技园区1008号')]
    for a in address:
        c = CourseOrg()
        c.name = '新东方学校, %s分校' %CityDict.objects.get(id = a[0])
        c.desc = '新东方教育，以外语培训和基础教育为核心，集教育培训、教育研发、图书杂志音响出版、出国留学服务、职业教育、在线教育、教育软件研发等于一体的大型综合性教育科技集团。'
        c.address = a[1]
        c.city = CityDict.objects.get(id = a[0])
        c.save()

    teacher_names = ['张继成','刘心武','赵宏军','吴凯文','刘素平','孙明杰','赵万东']
    for name in teacher_names:
        t = Teacher()
        t.org = CourseOrg.objects.get(id = random.randint(1, 3))
        t.name = name
        t.certificate_no = int('18'+''.join([str(random.randint(0,9)) for _i in range(16)])) # 共18位
        t.work_years = random.randint(5, 20)
        t.points = '设计新颖有趣的导入方式,激发学习欲望'  # 教学特点
        t.click_nums = random.randint(50, 100)  # 按点击数取前几名
        t.save()


    from course.models import Course, BannerCourse, Lesson, Video, CourseResource
    course_names = [('1','语文','http://img.ksbbs.com/asset/Mon_1703/05cacb4e02f9d9e.mp4'),\
                    ('2','数学','https://s3.bytecdn.cn/aweme/resource/web/static/image/index/tvc-v2_30097df.mp4'),\
                    ('3','英语','http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4'),\
                    ('4','政治','http://q4einq4ty.bkt.clouddn.com/1.mp4?e=1579691225&token=mVfiHbjs0mXxyFVLyr8lMigGjg7cDZ0ZZN6fPX9b:pNDsHXKVITnCm0wyI7PKqYIB8CM=')]
    for name in course_names:
        c = Course()
        c.name = name[1]
        c.desc = '%s 课程描述' %name[1]
        c.detail = '%s: 课程详情...' %name[1]
        c.course_org = CourseOrg.objects.get(id = random.randint(1, 3))
        c.teacher = Teacher.objects.get(id = random.randint(1, 4))
        c.category = random.choice(['公开课','试听','免费讲座']) # 课程类别
        c.degree = random.choice(['初级','中级','高级'])
        c.save()
        
    
    for name in course_names:
        l = Lesson()
        l.course = Course.objects.filter(name=name[1]).first()  
        l.name = '%s 第一章第一节' %name[1]
        l.save()
        
    for name in course_names:
        v = Video()
        v.lesson = Lesson.objects.get(id = name[0])
        v.name = '视频名: %s' %name[1]
        v.url = '%s' %name[2]
        v.save()
        
    for name in course_names:
        c = CourseResource()
        c.course = Course.objects.get(id = name[0])
        c.name = '课程资源名: %s' %name[1]
        c.save()
        

           
    
    from operation.models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse
          
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        u = UserAsk()
        u.name = name
        u.mobile =  '138' + ''.join([str(random.randint(0,9)) for _i in range(8)]) #后面的产生8位（0-9）的数
        u.course_name =  random.choice(course_names)
        u.save()
        
    ids = [1,2,3]
    for id in ids:
        c = CourseComments()
        c.user = UserProfile.objects.get(id = id)
        c.course = Course.objects.get(id = id)
        c.save() 
        
    for id in ids:
        c = UserFavorite() # 用户收藏
        c.user = UserProfile.objects.get(id = id)
        c.save()
        
    for id in ids:
        c = UserMessage()
        c.message = random.choice(['语文 message','数学 message','英语 message'])
        c.save()

    for id in ids:
        c = UserCourse()
        c.user = UserProfile.objects.get(id = id)
        c.course = Course.objects.get(id = id)
        c.save()
 
 
#    from users.models import Banner                
#     # 轮播图 从后台上传了
#     banner_names = [('1','语文','https://raw.githubusercontent.com/wuchunlong0/img/master/1_1200x478.jpg'),\
#                     ('2','数学','https://raw.githubusercontent.com/wuchunlong0/img/master/2_1200x478.jpg'),\
#                     ('3','英语','https://raw.githubusercontent.com/wuchunlong0/img/master/3_1200x478.jpg')]
#     
#     for name in banner_names:
#         b = Banner()
#         b.image = name[2]
#         b.title = name[1]
#         b.url = name[2]
#         b.index = name[0]
#         b.save()       
    
#   from django.contrib.auth.models import User
# 
#     # 创建超级用户 admin/admin
#     if not User.objects.filter(username = 'admin'):
#         User.objects.create_superuser('admin', 'admin@test.com','admin')
    #from basedao import BaseDAO
    #from app.models import School     #BaseDAO(School).delete({}) #删除全部记录    
    #BaseDAO(School).delete_batch([{'id':1},{'id':2}]) #删除仅保留ID=1 ID=2记录
    #BaseDAO(School).delete_batch_exclude({},{'id':2}) #删除仅保留ID=2的全部记录
    #terms = [({'name':'清华大学'},{'address':'中国北京'}),({'name':'复旦大学'},{'address':'中国上海'})]
    #BaseDAO(School).update_batch(terms)
    #BaseDAO(School).update_batch_exclude({},{},{'name':'大学','address':'中国'}) #将全部记录'name'更新为'大学'，'address'更新为'中国'                                                                    
    #print(BaseDAO(School).all()) 
    #print(BaseDAO(School).filter_exclude({'name':'北京大学'},{'address':'北京'}))                                                                     
                                                                         
                                                                         