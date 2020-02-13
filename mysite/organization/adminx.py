# organization/adminx.py

import xadmin

from .models import CityDict, CourseOrg, Teacher

# class TestAdmin(object):
#     '''测试'''
# 
#     list_display = ['name']
#     search_fields = ['name']
#     list_filter = ['name']

class CityDictAdmin(object):
    '''城市'''

    list_display = ['id','name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    '''机构'''

    list_display = ['id','name', 'desc', 'click_nums', 'fav_nums','add_time' ]
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums','city__name','address','add_time']


class TeacherAdmin(object):
    '''老师'''

    list_display = ['id', 'name','certificate_no','org', 'work_years', 'work_company','add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org__name', 'name', 'work_years', 'work_company','click_nums', 'fav_nums', 'add_time']

#xadmin.site.register(Test, TestAdmin)

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)