from selenium.webdriver.common.by import By

from pages.loginpage import Loginpage


class Homepage:
    def __init__(self,driver):
        self.driver = driver

    def adminmenu(self):
        self.driver.find_element(By.XPATH, "//img[@class='img-circle']").click()
        return self

    def logout(self):
        # from pages.loginpage import Loginpage #use here if circular import error is displayed and cut from top
        self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][2]").click()

        return Loginpage
