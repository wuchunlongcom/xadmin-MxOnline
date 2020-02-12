# MxOnline/urls.py

import xadmin

from django.urls import path,include,re_path

from django.views.generic import TemplateView
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView
from django.views.static import serve
from mysite.settings import MEDIA_ROOT
from users.views import LogoutView,IndexView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    
    path('login/',LoginView.as_view(),name = 'login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('captcha/',include('captcha.urls')),
    
    # 激活用户(邮箱注册)
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    
    # 忘记密码(修改密码)
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    # 修改密码
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIA_ROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),

    # 课程机构app相关url配置
    path("org/", include('organization.urls', namespace="org")),
    
    # 课程app相关url配置
    path("course/", include('course.urls', namespace="course")),

    #个人信息
    path("users/", include('users.urls', namespace="users")),
    #静态文件
    # re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATICFILES_DIRS }),

    # 富文本相关url
    path('ueditor/',include('DjangoUeditor.urls' )),
    
    path('', IndexView.as_view(),name='index'),
]

# 全局404页面配置
handler404 = 'users.views.pag_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'