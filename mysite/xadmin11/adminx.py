from __future__ import absolute_import
import xadmin
from .models import UserSettings, Log
from xadmin.layout import *

from django.utils.translation import ugettext_lazy as _, ugettext

class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

xadmin.site.register(UserSettings, UserSettingsAdmin)


class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'  # 日志图标
    
# 日志注册
xadmin.site.register(Log, LogAdmin)

# add
from django.template import loader 
from xadmin.views import BaseAdminPlugin, ListAdminView
from xadmin.plugins.utils import get_context_dict

class LinkAdminPlugin(BaseAdminPlugin): 
    """ 
        块视图应用 添加自定义工具栏toolbar 
    """ 
       
    add_form_button = False  
      
    def init_request(self, *args, **kwargs):  
        return bool(self.add_form_button)  
      
    # my_top_toolbar为xadmin model_list.html中存在的view_block区块  
    def block_my_top_toolbar(self, context, nodes):  
        nodes.append(loader.render_to_string(
            'my-define/add_form_button.html',\
            context=get_context_dict(context)))  

xadmin.site.register_plugin(LinkAdminPlugin, ListAdminView)  

'''
块视图  layout.py

'''