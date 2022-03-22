from selenium.webdriver.common.by import By


class LoginPageLocs:
    # 用户名
    userName_loc = (By.XPATH, '//*[@id="userName"]')
    # 登录按钮
    login_loc = (By.XPATH, '//*[@class="vam ml5"]')
    # 手机号输入框
    phone_loc = (By.XPATH, '//input[@id="u-email"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@placeholder="请输入密码"]')
    # 登陆按钮
    login_button_loc = (By.XPATH, '//*[@class="e-login-btn" and @title="登 录"]')
    # 登陆区域的提示框
    error_tips_from_login_area = (By.XPATH, '//*[@class="icon16 u-a-cw"]')
    # 关闭登录按钮
    close_login_loc = (By.XPATH, '//a[@id="dClose"]')
    # qq登录按钮
    qqlogin_button_loc = (By.XPATH, '//a[@title="QQ登录"]')
