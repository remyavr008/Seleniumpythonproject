import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.adminpage import Adminpage
from pages.loginpage import Loginpage
from utilities.Excelutility import ExcelUtility


class Testadmin:

    def test_admin(self,browserinstance):
        self.driver = browserinstance

        excelutilit=ExcelUtility("D:/Pytestexcel/testdata.xlsx")
        time.sleep(5)
        uname = excelutilit.get_string_data(2,1,"Sheet1")
        pwd = excelutilit.get_string_data(2,2,"Sheet1")
        time.sleep(5)
        """self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        time.sleep(5)
        self.driver.maximize_window()"""
        time.sleep(3)
        login1 = Loginpage(self.driver)
        login1.enterusername(uname).enterpassword(pwd).login()
        """
        login1 = Loginpage(self.driver)
        login1.enterusername(uname)
        login1.enterpassword(pwd)
        login1.login()
        self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text()='Sign In']").click()
        time.sleep(3)
        #self.driver.find_element(By.XPATH,"//p[text()='Admin Users']").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Users").click()
        time.sleep(5)"""

        manage = Adminpage(self.driver)
        manage.adminusers().manageusers().newuser().newuserdetails().newusercreate()
        #manage.newuserdetails()
        #manage.newusercreate()
        time.sleep(5)

        """
        time.sleep(5)
        manage.manageusers()
        time.sleep(5)
        manage.newuser()
        manage.newuserdetails()
        manage.newusercreate()

        self.driver.find_element(By.XPATH,"//p[text()='Manage Users']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//a[text()=' New']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@id='username']").send_keys("us1")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("pwd1")
        time.sleep(5)
        dropdown = self.driver.find_element(By.XPATH,"//select[@id='user_type']")
        sel = Select(dropdown)
        sel.select_by_value('staff')
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[@name='Create']").click()
        time.sleep(5)"""
        self.driver.close()


    def test_reset(self,browserinstance):
        self.driver = browserinstance
        excelutilit = ExcelUtility("D:/Pytestexcel/testdata.xlsx")
        time.sleep(5)
        uname = excelutilit.get_string_data(2, 1, "Sheet1")
        pwd = excelutilit.get_string_data(2, 2, "Sheet1")
        time.sleep(5)
        """self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)"""
        login1 = Loginpage(self.driver)
        login1.enterusername(uname).enterpassword(pwd).login()

        manage = Adminpage(self.driver)
        manage.adminusers()
        time.sleep(5)
        manage.manageusers()
        time.sleep(5)
        manage.newuser()
        manage.newuserdetails()
        manage.resetuser()

        """self.driver.find_ element(By.XPATH, '//input[@placeholder="Username"]').send_keys(uname)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(pwd)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        time.sleep(3)
        # self.driver.find_element(By.XPATH,"//p[text()='Admin Users']").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Users").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//p[text()='Manage Users']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[text()=' New']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("us2")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("pwd2")
        time.sleep(5)
        dropdown = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
        sel = Select(dropdown)
        sel.select_by_value('staff')
        time.sleep(3)
        #self.driver.find_element(By.XPATH,"//a[text()='Reset'][2]").click()
        self.driver.find_element(By.XPATH,"//i[@class='ace-icon fa fa-sync-alt']").click()
        time.sleep(10)"""
        self.driver.close()

