'''
初步体验交互式Python编程
'''

print('欢迎来此新世界')

username = input('请输入您的用户名：')
password = input('请输入您的密码：')

if username and password:
    print('登录成功，您的账号->username,密码是password')
else:
    if not username:
        print('用户名不能为空')

    if not password:
        print('密码不能为空')
