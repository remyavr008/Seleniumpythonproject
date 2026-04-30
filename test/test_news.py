import time


import pytest
from selenium.webdriver.common.by import By

from pages.loginpage import Loginpage
from pages.newspage import Newspage
from utilities.Excelutility import ExcelUtility


class Testnews:

    def test_managenewshome(self,browserinstance):
        self.driver = browserinstance

        excelutilit=ExcelUtility("D:/Pytestexcel/testdata.xlsx")

        time.sleep(3)
        uname = excelutilit.get_string_data(2,1,"Sheet1")
        pwd = excelutilit.get_string_data(2,2,"Sheet1")
        time.sleep(3)
        """self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        time.sleep(5)
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()='Sign In']").click()
        time.sleep(5)"""

        login1 = Loginpage(self.driver)
        login1.enterusername(uname).enterpassword(pwd).login()

        self.driver.find_element(By.XPATH,"//a[text() ='More info ']//following::p[text()='Manage News']").click()
        self.driver.find_element(By.XPATH,"(//i[@class='fas fa-arrow-circle-right'])[7]").click()

        time.sleep(5)
        self.driver.find_element(By.XPATH,'//a[text()="Home"]').click()


        self.driver.close()

    def test_save(self,browserinstance):
        self.driver=browserinstance
        excelutilit=ExcelUtility("D:/Pytestexcel/testdata.xlsx")

        time.sleep(3)
        uname = excelutilit.get_string_data(2,1,"Sheet1")
        pwd = excelutilit.get_string_data(2,2,"Sheet1")
        time.sleep(3)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        time.sleep(5)
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()='Sign In']").click()
        time.sleep(5)
        news1 = Newspage(self.driver)
        news1.Moreinfo_news()
        news1.savenews()
        """self.driver.find_element(By.XPATH,"(//i[@class='fas fa-arrow-circle-right'])[7]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//a[text()=" New"]').click()
        time.sleep(3)
        self.driver.find_element(By.ID,"news").send_keys("This is test news")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text()='Save']").click()
        time.sleep(3)"""

    def test_search(self,browserinstance):
        self.driver=browserinstance
        excelutilit = ExcelUtility("D:/Pytestexcel/testdata.xlsx")

        time.sleep(3)
        uname = excelutilit.get_string_data(2, 1, "Sheet1")
        pwd = excelutilit.get_string_data(2, 2, "Sheet1")
        time.sleep(3)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        time.sleep(5)
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        time.sleep(3)
        news1 = Newspage(self.driver)
        news1.Moreinfo_news()
        news1.searchnews()
        #self.driver.find_element(By.XPATH, "(//i[@class='fas fa-arrow-circle-right'])[7]").click()
        #time.sleep(3)
        """self.driver.find_element(By.XPATH, '//a[text()=" New"]').click()
        time.sleep(3)
        self.driver.find_element(By.ID, "news").send_keys("This is to search")
        time.sleep(3)"""
        """self.driver.find_element(By.XPATH, '//i[@class=" fa fa-search"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("search")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//button[@name="Search"]').click()
        time.sleep(3)"""