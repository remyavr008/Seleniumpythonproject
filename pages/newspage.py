import time

from selenium.webdriver.common.by import By

from pages.adminpage import Adminpage


class Newspage:
    def __init__(self,driver):
        self.driver = driver
        self.moreinfo = (By.XPATH, "(//i[@class='fas fa-arrow-circle-right'])[7]")

    def Moreinfo_news(self):
        self.driver.find_element(*self.moreinfo).click()
        #elf.driver.find_element(By.XPATH, "(//i[@class='fas fa-arrow-circle-right'])[7]").click()
        time.sleep(3)
        return self.driver

    def savenews(self):
        self.driver.find_element(By.XPATH, '//a[text()=" New"]').click()
        time.sleep(3)
        self.driver.find_element(By.ID, "news").send_keys("This is test news")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(3)
        return self

    def searchnews(self):
        self.driver.find_element(By.XPATH, '//i[@class=" fa fa-search"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("news")
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//button[@name="Search"]').click()
        time.sleep(3)

