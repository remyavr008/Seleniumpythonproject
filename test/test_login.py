import time

import pytest
from selenium.webdriver.common.by import By

from constant import constants
from constant.constants import loginurl
from pages.loginpage import Loginpage
from utilities.Excelutility import ExcelUtility

#In this file, the values are replaced with constants also for sheetname,filepath and url

class TestLogin:
    @pytest.mark.order(2)
    def test_validlogin(self,browserinstance):
        self.driver = browserinstance

        #excelutilit=ExcelUtility("D:/Pytestexcel/testdata.xlsx")
        excelutilit=ExcelUtility(constants.file_path)

        time.sleep(5)
        uname = excelutilit.get_string_data(2,1,constants.sheetname)
        pwd = excelutilit.get_string_data(2,2,constants.sheetname)
        time.sleep(5)
        #self.driver = browserinstance
        #self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        #self.driver.get(loginurl)
        time.sleep(5)
        login1 = Loginpage(self.driver)
        login1.enterusername(uname).enterpassword(pwd).login() #Chaining is used here to reduce the no of loc to be executed
        #login1.enterpassword(pwd)
        #login1.login()
        """
        self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()='Sign In']").click() """
        assert self.driver.current_url == "https://groceryapp.uniqassosiates.com/admin"
        time.sleep(5)
        #self.driver.close()

    @pytest.mark.order(1)
    def test_invalidusnamelogin(self,browserinstance):
        self.driver = browserinstance
        
        excelutilit=ExcelUtility(constants.file_path)

        time.sleep(5)
        uname = excelutilit.get_string_data(3,1,constants.sheetname)
        pwd = excelutilit.get_string_data(3,2,"Sheet1") #"Sheet1"To be replaced with constants.sheetname
        time.sleep(5)
        #self.driver.get(loginurl)
        time.sleep(5)
        login1 = Loginpage(self.driver)
        login1.enterusername(uname).enterpassword(pwd).login()
        """
        login1.enterusername(uname)
        login1.enterpassword(pwd)
        login1.login()
        
        self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()='Sign In']").click()
        time.sleep(5)"""
        assert self.driver.current_url == "https://groceryapp.uniqassosiates.com/admin/login"
        self.driver.close()

    @pytest.mark.order(3)
    def test_invalidpwdlogin(self,browserinstance):
        self.driver = browserinstance
        excelutilit=ExcelUtility("D:/Pytestexcel/testdata.xlsx")

        time.sleep(5)
        uname = excelutilit.get_string_data(4,1,constants.sheetname)
        pwd = excelutilit.get_string_data(4,2,constants.sheetname)
        time.sleep(5)
        #removed browser url
        login1 = Loginpage(self.driver)
        login1.enterusername(uname).enterpassword(pwd).login()
        """
        login1.enterpassword(pwd)
        login1.login()
        
        self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()='Sign In']").click()
        time.sleep(5)"""
        assert self.driver.current_url == "https://groceryapp.uniqassosiates.com/admin/login"
        self.driver.close()

    @pytest.mark.order(4)
    def test_invalidcredentials(self,browserinstance):
        self.driver = browserinstance

        excelutilit=ExcelUtility("D:/Pytestexcel/testdata.xlsx")

        time.sleep(5)
        uname = excelutilit.get_string_data(5,1,constants.sheetname)
        pwd = excelutilit.get_string_data(5,2,constants.sheetname) #constants.sheetname can also be written directly as "Sheet1"
        time.sleep(5)

        login1 = Loginpage(self.driver)
        login1.enterusername(uname).enterpassword(pwd).login()
        """
        login1.enterusername(uname)
        login1.enterpassword(pwd)
        login1.login()
        
        self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()='Sign In']").click()"""
        assert self.driver.current_url == "https://groceryapp.uniqassosiates.com/admin/login"
        time.sleep(5)
        self.driver.close()




