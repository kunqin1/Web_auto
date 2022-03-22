"""
1、等待元素可见
2、查找元素
3、点击操作：等待 - 查找 - 点击
4、输入操作：等待 - 查找 - 输入
5、获取元素文本：等待 - 查找 - 获取文本
6、获取元素属性：等待 - 查找 - 获取属性值

节省代码量、记录日志、失败截图

7、窗口切换 -- 让新窗口出现，获取所有句柄，切换到新窗口。
"""
import allure
import os
import time

from appium.webdriver import webdriver

from Common.my_logger import logger
from Common.handle_path import screenshot_dir
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class Basepage:
    # web自动化
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_ele_visible(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        等待元素可见
        :param locator: 元素定位器
        :param page_action: 页面操作
        :param timeout: 过期时间
        :param poll_frequency: 每次查找的时间
        :return:
        """
        logger.info("在 {} 行为，等待元素：{} 可见。".format(page_action, locator))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            # 输出到日志
            logger.exception("等待元素 {} 可见失败！".format(locator))
            # 失败截取当前页面
            self.get_page_img(page_action)
            raise
        else:
            end = time.time()
            logger.info("等待耗时为：{}".format(end - start))

    def wait_page_contains_element(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        等待元素存在
        :param locator:元素定位器
        :param page_action:页面操作
        :param timeout:
        :param poll_frequency:
        :return:
        """
        logger.info("在 {} 行为，等待元素：{} 存在。".format(page_action, locator))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except:
            # 输出到日志
            logger.exception("等待元素 {} 存在失败！".format(locator))
            # 失败截取当前页面
            self.get_page_img(page_action)
            raise
        else:
            end = time.time()
            logger.info("等待耗时为：{}".format(end - start))

    def get_element(self, locator, page_action, timeout=20, poll_frequency=0.5, wait=None):
        """
        元素定位
        :param locator: 元素定位器
        :param page_action: 页面操作
        :param timeout:
        :param poll_frequency:
        :param wait:
        :return:
        """
        # 先等待元素可见或者存在
        if wait:
            self.wait_page_contains_element(locator, page_action, timeout, poll_frequency)
        else:
            self.wait_ele_visible(locator, page_action, timeout, poll_frequency)

        logger.info("在 {} 行为，查找元素：{}".format(page_action, locator))
        try:
            ele =self.driver.find_element(*locator)
            # ele = self.driver.find_element(*locator)
        except:
            # 输出到日志
            logger.exception("查找元素失败！")
            # 失败截取当前页面
            self.get_page_img(page_action)
            raise
        else:
            return ele

    def get_elements(self, locator, page_action, timeout=20, poll_frequency=0.5, wait=None):
        """

        :param locator: 元素定位器
        :param page_action: 页面操作
        :param timeout:
        :param poll_frequency:
        :param wait:
        :return:
        """
        # 先等待元素可见或者存在
        if wait:
            self.wait_page_contains_element(locator, page_action, timeout, poll_frequency)
        else:
            self.wait_ele_visible(locator, page_action, timeout, poll_frequency)

        logger.info("在 {} 行为，查找元素：{}".format(page_action, locator))
        try:
            ele = self.driver.find_elements(*locator)
        except:
            # 输出到日志
            logger.exception("查找元素失败！")
            # 失败截取当前页面
            self.get_page_img(page_action)
            raise
        else:
            return ele

    def click_element(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        点击元素操作
        :param locator: 元素的定位表达式
        :param page_action: 操作名称
        :param timeout:
        :param poll_frequency:
        :return:
        """

        # 等待 - 查找
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        # 点击
        logger.info("在 {} 行为，点击元素：{}".format(page_action, locator))
        try:
            ele.click()
        except:
            logger.exception("点击元素失败！")
            self.get_page_img(page_action)
            raise

    def input_text(self, locator, page_action, value, timeout=20, poll_frequency=0.5):
        """
        输入文本
        :param locator: 元素定位器
        :param page_action: 操作页面
        :param value: 输入的值
        :param timeout:
        :param poll_frequency:
        :return:
        """
        # 等待 - 查找
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("在 {} 行为，给元素：{} 输入文本值：{}".format(page_action, locator, value))
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            logger.exception("元素输入文本失败！")
            self.get_page_img(page_action)
            raise

    def get_text(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        获取文本
        :param locator: 定位器
        :param page_action: 页面操作
        :param value:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("在 {} 行为，获取元素：{} 文本值".format(page_action, locator))
        try:
            res = ele.text
        except:
            logger.exception("获取元素文本失败！")
            self.get_page_img(page_action)
            raise
        else:
            return res

    def get_attribute(self, locator, page_action, attr, timeout=20, poll_frequency=0.5):
        """
        获取元素的属性
        :param poll_frequency:
        :param timeout:
        :param page_action:
        :param locator:
        :param loc: 元素的定位器
        :param attr: 属性名
        :param desc: 元素的描述
        :return:
        """
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("在 {} 行为，获取元素：{} 属性：{}".format(page_action, locator, attr))
        try:
            res = ele.get_attribute(attr)
        except:
            logger.exception("获取元素属性失败！")
            self.get_page_img(page_action)
            raise
        return res

    def switch_to_iframe_loc(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        元素定位器类型的iframe切换
        :param locator: 元素定位器
        :param page_action: 元素操作
        :param timeout:
        :param poll_frequency:
        :return:
        """
        logger.info("在 {} 行为中，等待 {} iframe出现并切换".format(page_action, locator))
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(locator)
            )
        except:
            logger.exception("等待iframe可见并切换失败")
            self.get_page_img(page_action)
            raise

    def open_new_window_and_switch(self, url, page_action, timeout=20, poll_frequency=0.5):
        logger.info("在 {} 行为中，打开新窗口并切换".format(page_action))
        old_win = self.driver.window_handles
        try:
            js = 'window.open(arguments[0])'
            self.driver.execute_script(js, url)
            # 等待窗口打开
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.new_window_is_opened(old_win)
            )
            new_wins = self.driver.window_handles
            self.driver.switch_to.window(new_wins[-1])
        except:
            logger.exception("切换新窗口失败")
            self.get_page_img(page_action)
            raise

    def switch_to_iframe_name(self, name, page_action):
        """
        使用iframe name方式切换iframe标签
        :param name:
        :param page_action:
        :return:
        """
        logger.info("在 {} 行为中，等待 {} iframe出现并切换".format(page_action, name))
        try:
            self.driver.switch_to.frame(name)
        except:
            # 记录日志
            logger.exception("等待iframe可见并进行切换失败")
            # 失败截图
            self.get_page_img(page_action)
            raise

    def get_page_img(self, page_action):
        # 命令规范: {XX页面_XX操作}_截图时间.png
        cur_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        file_path = os.path.join(screenshot_dir, "{}_{}.png".format(page_action, cur_time))
        try:
            self.driver.save_screenshot(file_path)
        except:
            logger.error("对 {} 操作进行截图失败".format(page_action))
            raise
        else:
            # 将错误截图放入allure报告中
            with open(file_path, 'rb') as f:
                file = f.read()
                allure.attach(file, "失败截图", allure.attachment_type.PNG)
            logger.error("对 {} 操作进行截图成功".format(page_action))
            logger.info("截图保存在：{}".format(file_path))

    def Scroll_element_visible(self, locator, page_action):
        """
        :param locator: 元素定位器
        :param page_action:
        :return:
        """
        ele = self.get_element(locator, page_action)
        logger.info("滑动元素 {} 到可见操作".format(page_action))
        try:
            js = 'arguments[0].scrollIntoView()'
            driver.execute_script(js, ele)
        except:
            logger.exception("滑动到{}可见失败".format(page_action))
            raise


if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep

    driver = webdriver.Chrome()
    base = Basepage(driver)
    driver.get("http://www.baidu.com")
    # 等待输入框可见
    url = "http://www.lemonban.com/"
    loc_button = ("id", "su")
    base.open_new_window_and_switch(url, "切换到柠檬班官网")
    sleep(7)
    driver.quit()
