from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from Common import basepage
from PageLocators.login_page_locs import LoginPageLocs as loc


class LoginPage:
    # 属性 - 元素定位

    def __init__(self, driver: webdriver):
        self.driver = basepage.Basepage(driver)
        self.wait = WebDriverWait(driver, 20)

    def login(self, phone, passwd):
        self.driver.click_element(loc.login_loc, "点击首页登录按钮")
        self.driver.input_text(loc.phone_loc, "输入手机号、邮箱", phone)
        self.driver.input_text(loc.passwd_loc, "输入密码", passwd)
        self.driver.click_element(loc.login_button_loc, "点击登录按钮")

    def get_error_msg_from_login_area(self):
        """
        获取登陆失败时，在登陆区域的提示。
        :return:
        """
        # self.wait.until(EC.visibility_of_element_located(loc.error_tips_from_login_area))
        try:
            self.driver.wait_ele_visible(loc.error_tips_from_login_area, "等待登录失败提示出现")
            text = self.driver.get_text(loc.error_tips_from_login_area, "获取错误的信息")
        except:
            self.driver.get_page_img("获取错误信息用例失败截图")
            return "False"
        else:
            return text

    def get_userName(self):
        """
        登录成功后，获取用户名
        :return:
        """
        try:
            self.driver.get_element(loc.userName_loc, "查看登录后，用户名是否存在")
        except:
            self.driver.get_page_img("登录失败用例失败截图")
            return False
        else:
            return True

    def close_login_window(self):
        """
        点击登录后关闭登录弹窗
        :return:
        """
        self.driver.click_element(loc.close_login_loc, "关闭登录弹窗")

