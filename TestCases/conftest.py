import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from TestDatas import global_datas as gd


def create_driver(is_headers=True):
    """
    启动driver:默认启动浏览器窗口，is_header设置为false则为无头模式运行
    1、无头模式运用与，在服务器上跑自动化代码，因为不能打开浏览器
    2、用例跑起来更快,节约时间
    :param is_headers: True 或者 False
    :return: driver对象
    """
    if is_headers:
        driver = webdriver.Chrome()
    else:
        # 设置无头浏览器模式
        options = ChromeOptions()
        options.add_argument('--headless')
        # 设置窗口大小，解决无头浏览器模式无法最大窗口问题
        options.add_argument('windows-size=1920,1050')
        driver = webdriver.Chrome(options=options)
    return driver


# 定义fixture - 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def login():
    # 实例化driver,访问登陆页面
    driver = create_driver(is_headers=True)
    driver.get(gd.login_url)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def back_login(login):
    login.get(gd.login_url)
    yield login





