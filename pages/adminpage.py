import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Adminpage:
    def __init__(self,driver):
        self.driver = driver
        self.admnuser = (By.PARTIAL_LINK_TEXT, "Users")
        self.mguser = (By.XPATH, "//p[text()='Manage Users']")
        self.nwuser = (By.XPATH, "//a[text()=' New']")
        self.nwuname = (By.XPATH, "//input[@id='username']")
        self.nwpsd = (By.XPATH, "//input[@id='password']")
        self.drop1 = (By.XPATH, "//select[@id='user_type']")
        self.nwusrcreate = (By.XPATH, "//button[@name='Create']")
        self.reset = (By.XPATH,"//*[@id='adddiv']/div/div/div/form/div[2]/a")
        #pageutil = self.Pageutility



    def adminusers(self):
        #self.driver.find_element(By.PARTIAL_LINK_TEXT, "Users").click()
        self.driver.find_element(*self.admnuser).click()
        return self
        time.sleep(5)


    def manageusers(self):
        #self.driver.find_element(By.XPATH, "//p[text()='Manage Users']").click()
        self.driver.find_element(*self.mguser).click()
        return self
        time.sleep(5)

    def newuser(self):
        self.driver.find_element(*self.nwuser).click()
        #self.driver.find_element(By.XPATH, "//a[text()=' New']").click()
        return self
        time.sleep(5)

    def newuserdetails(self):
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))#Written to generate random text for username to avoid error
        self.driver.find_element(*self.nwuname).send_keys(random_text)
        #self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(random_text)
        #self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("us2")
        time.sleep(5)
        #self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("pwd2")
        self.driver.find_element(*self.nwpsd).send_keys("pwd2")
        time.sleep(5)
        #dropdown = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
        dropdown = self.driver.find_element(*self.drop1)
        sel = Select(dropdown)
        #self.pageutility.selectdata()
        sel.select_by_value('staff')
        time.sleep(5)
        return self

    def newusercreate(self):
        self.driver.find_element(*self.nwusrcreate).click()
        #self.driver.find_element(By.XPATH, "//button[@name='Create']").click()
        return self
        time.sleep(5)

    def resetuser(self):
        #self.driver.find_element(By.XPATH, "//i[@class='ace-icon fa fa-sync-alt']").click() # Main reset button
        self.driver.find_element(*self.reset).click()
        time.sleep(10)
