# -*- coding: UTF-8 -*-

# 数据库增、删、改
class BaseDAO:
    def __init__(self, model):
        self.MODEL_CLASS = model
        self.SAVE_BATCH_SIZE = 50

    def save(self, obj):
        """
           保存一条记录
           obj：{'name':'清华大学','address':'北京'}
        """
        self.MODEL_CLASS(**obj).save()        

    def save_batch(self, objs):
        """ 
            保存多条记录
           objs:[{'name':'清华大学','address':'北京'},{'name':'复旦大学','address':'上海'}]
        """
        items = [self.MODEL_CLASS(**d) for d in objs]
        self.MODEL_CLASS.objects.bulk_create(items, batch_size=self.SAVE_BATCH_SIZE)        

    def delete(self, obj):
        """
            删除一条记录（等于删除）
            obj：{'name':'清华大学','address':'北京'} 删除'name'='清华大学','address'='北京'记录、  
                {'id':2} 删除id=2记录
                {} 删除全部记录
        """
        self.MODEL_CLASS.objects.filter(**obj).delete()       

    def delete_batch(self, objs):
        """
            批量删除记录（等于删除）
            objs:[{'name':'清华大学','address':'北京'},{'name':'复旦大学','address':'上海'}]
                [{'id':1},{'id':2}]
        """
        for obj in objs:
            self.delete(obj)

    def delete_batch_exclude(self, filter_dict, exclude_dict):
        """
            批量删除记录（等于删除 and 不等于删除）
            BaseDAO(School).delete_batch_exclude({},{'id':2}) 删除仅保留ID=2的全部记录
        """
        self.MODEL_CLASS.objects.filter(**filter_dict).exclude(**exclude_dict).delete()

    def update(self, filter_dict, update_dict):
        """
            更新（等于更新）
            filter_dict：{'name':'清华大学'},   update_dict：{'address':'中国北京'}
        """               
        self.MODEL_CLASS.objects.filter(**filter_dict).update(**update_dict)

    def update_batch(self, objs):
        """
            批量更新（等于更新）
            objs:[({'name':'清华大学'},{'address':'中国北京'}),({'name':'复旦大学'},{'address':'中国上海'})]
        """       
        
        for filter_dict, update_dict in objs:
            self.update(filter_dict, update_dict)

    def update_batch_exclude(self, filter_dict, exclude_dict, update_dict):
        """
            批量更新（等于更新 and 不等于更新）
            filter_dict:{}     =
            exclude_dict:{}    !=
            update_dict:{'name':'大学','address':'中国'}
            
            BaseDAO(School).update_batch_exclude({},{},{'name':'大学','address':'中国'})
            将全部记录'name'更新为'大学'，'address'更新为'中国'
        """
        self.MODEL_CLASS.objects.filter(**filter_dict).exclude(**exclude_dict).update(**update_dict)

    def filter_exclude(self, filter_dict, exclude_dict):
        """
            精确查找记录
            filter_dict：{'name':'清华大学'},   exclude_dict：{'address':'中国北京'}
        """
        return self.MODEL_CLASS.objects.filter(**filter_dict).exclude(**exclude_dict)

    def filter(self, filter_dict):
        """
            精确查找记录
            filter_dict：{'name':'清华大学'}
        """
        return self.MODEL_CLASS.objects.filter(**filter_dict)

    def filter_name_i(self, name):
        """
            模糊(包含)查找字段name 
            name：'大学'  查找字段为name为'大学'的记录
        """
        return self.MODEL_CLASS.objects.filter(name__icontains=name)
    
    def filter_date_start(self, date):
        """
            查找大于等于日期date 
            date：2019-05-05  查找大于2019-05-05的记录
        """
        return self.MODEL_CLASS.objects.filter(date__gte = date)

    def filter_date_end(self, date):
        """
            查找小于等于日期date 
            date：2019-05-05  查找小于2019-05-05的记录
        """
        return self.MODEL_CLASS.objects.filter(date__lte = date)
    
    def all(self):
        """
            查找全部
        """
        return self.MODEL_CLASS.objects.all() 


'''
https://www.codercto.com/a/25589.html
https://blog.csdn.net/GodnessIsMyMine/article/details/85128036
'''