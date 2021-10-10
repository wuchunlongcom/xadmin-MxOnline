# MxOnline  在线教育平台
## 环境
```
python 3.7.5
django版本: 2.2.6。

./start.sh -i
http://localhost:8000/
http://localhost:8000/xadmin/     admin/admin
```
###需要从后台上传有关图像,才能看效果。参见（有道云笔记）：xadmin-MxOnline说明书

```
一、上传图像
1、上传轮播图
http://localhost:8000/xadmin/     admin/admin

【轮播图】-【增加 轮播图】:桌面--图片4张 1_1200x478.jpg -- 4_1200x478.jpg

2、上传课程封面图图像  语文、 数学、英语、政治   应该233x190     
3、上传课程图像（轮播图像）应该  470x300   实际470x300

```
```
系统介绍：

    系统具有完整的用户登录注册以及找回密码功能，拥有完整个人中心。
    个人中心: 修改头像，修改密码，修改邮箱，可以看到我的课程以及我的收藏。可以删除收藏，我的消息。
    导航栏: 公开课，授课讲师，授课机构，全局搜索。
    点击公开课--> 课程列表，排序-搜索。热门课程推荐，课程的分页。
    点击课程--> 课程详情页中对课程进行收藏，取消收藏。富文本展示课程内容。
    点击开始学习--> 课程的章节信息，课程的评论信息。课程资源的下载链接。
    点击授课讲师-->授课讲师列表页，对讲师进行人气排序以及分页，右边有讲师排行榜。
    点击讲师的详情页面--> 对讲师进行收藏和分享，以及讲师的全部课程。
    导航栏: 授课机构有分页，排序筛选功能。
    机构列表页右侧有快速提交我要学习的表单。
    点击机构--> 左侧：机构首页,机构课程，机构介绍，机构讲师。
    后台管理系统可以切换主题。左侧每一个功能都有列表显示, 增删改查，筛选功能。
    课程列表页可以对不同字段进行排序。选择多条记录进行删除操作。
    课程列表页：过滤器->选择字段范围等,搜索,导出csv，xml，json。
    课程新增页面上传图片，富文本的编辑。时间选择，添加章节，添加课程资源。
    日志记录：记录后台人员的操作
```

```
### Django项目在线教育平台网站的实战开发
(一） https://blog.csdn.net/qq_41782425/article/details/89788542
(二）官方源码 ：https://github.com/mtianyan/Mxonline3

### 简书学习的代码
### 参考文档 https://www.jianshu.com/p/ec284482fc89
### 简书学习的源码 https://github.com/iSk2y/LearnMxOnline.git

### 参考源码 xadmin下载地址
[点击下载](https://github.com/sshwsfc/xadmin/tree/django2) <br/> 


### 播放视频网址
https://s3.bytecdn.cn/aweme/resource/web/static/image/index/tvc-v2_30097df.mp4 </br>
把上面链接复制到视频--“访问地址” 里面就可以播放了。
```

## Generate static files
```
cd ../mysite
rm -rf static
python manage.py collectstatic
```

