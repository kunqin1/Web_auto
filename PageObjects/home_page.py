from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from PageLocators.home_page_locs import HomePageLocs as loc


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)

    def is_exit_exist(self):
        """
        如果存在，则返回True,如果不存在，则返回False
        :return:
        """
        try:
            self.wait.until(EC.visibility_of_element_located(loc.exit_loc))
        except:
            return False
        else:
            return True
