# 登陆成功的测试数据
valid_user = ("18782048139", "123456789")

# 登陆失败的数据 - 用户名为空/密码为空/用户格式不正确
invalid_data = [
    {"user": "", "passwd": "", "check": "请输入账号/邮箱/手机号！"},
    {"user": "18684720553", "passwd": "", "check": "请输入登录密码！"},
    {"user": "1868472055", "passwd": "python", "check": "帐号或密码错"},
    # {"user": "186847205531", "passwd": "python", "check": "请输入手机号"}
]
