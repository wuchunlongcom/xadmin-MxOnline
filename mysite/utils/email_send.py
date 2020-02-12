# apps/utils/email_send.py

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from mysite.settings import EMAIL_FROM

# 生成随机字符串
def random_str(random_length=8):
    str = ''
    # 生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str

# 发送邮件（默认发送注册邮件）
def send_register_eamil(email, send_type="register"):
    # 发送之前先保存到数据库，到时候查询链接是否存在
    # 实例化一个EmailVerifyRecord对象
    email_record = EmailVerifyRecord()
    # 生成随机的code放入链接
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()

    # 定义邮件内容:
    email_title = ""
    email_body = ""
    url = 'http://localhost:8000' # 'http://106.15.58.198'
    # 发送注册邮件（激活用户）
    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "空" #"请点击下面的链接, 激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)
        msg = "请点击下面的链接, 激活你的账号: <a href='{0}/{1}/{2}' target='_blank'> {0}/{1}/{2} </a> ".format(url,'active',code)
        # 使用Django内置函数完成邮件发送。
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email], html_message=msg)
        # 如果发送成功
        if send_status:
            pass
    # 忘记密码(修改密码)
    elif send_type == "forget":
        email_title = "修改密码链接"
        email_body = "空" 
        msg = "请点击下面的链接, 设置你的新密码: <a href='{0}/{1}/{2}' target='_blank'> {0}/{1}/{2} </a> ".format(url,'reset',code)
        # 使用Django内置函数完成邮件发送。主题，    邮件内容，   从哪里发，  接受者list，  超链接
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email], html_message=msg)
        # 如果发送成功
        if send_status:
            pass

    elif send_type == "update_email":
        email_title = "邮箱修改验证码"
        email_body = "你的邮箱验证码为{0}".format(code)

        # 使用Django内置函数完成邮件发送。
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            pass