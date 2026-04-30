import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from constant import constants
from pages.homepage import Homepage
from pages.loginpage import Loginpage
from utilities.Excelutility import ExcelUtility


class TestLogout:
    """def test_validlogin(self,crossbrowser):
        self.driver = crossbrowser"""
    def test_logout(self,browserinstance):
        self.driver = browserinstance

        excelutilit=ExcelUtility("D:/Pytestexcel/testdata.xlsx")
        time.sleep(5)
        uname = excelutilit.get_string_data(2,1,"Sheet1")
        pwd = excelutilit.get_string_data(2,2,constants.sheetname)
        time.sleep(5)


        """self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()='Sign In']").click()
        time.sleep(5)"""
        login1 = Loginpage(self.driver)
        login1.enterusername(uname).enterpassword(pwd).login().adminmenu().logout()
        #login returns homepage ,so no need to create a new object for Homepage
        """login1.enterpassword(pwd)
        login1.login()"""
        """assert self.driver.current_url== "https://groceryapp.uniqassosiates.com/admin"

        home = Homepage(self.driver)
        home.adminmenu()
        home.logout()"""
        assert  self.driver.current_url == "https://groceryapp.uniqassosiates.com/admin/login"


        """self.driver.find_element(By.XPATH,"//img[@class='img-circle']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//a[@class='dropdown-item'][2]").click()
        time.sleep(3)"""
        self.driver.close()
