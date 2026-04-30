import self
from selenium.webdriver.common.by import By




class Loginpage:
    def __init__(self,driver):
        self.driver = driver
        self.usernamelocator = (By.XPATH, '//input[@placeholder="Username"]')
        self.passwordlocator = (By.XPATH, '//input[@placeholder="Password"]')
        self.loginlocator = (By.XPATH, "//button[text()='Sign In']")

    def enterusername(self,uname):
        #self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(uname)
        self.driver.find_element(*self.usernamelocator).send_keys(uname)
        return self

    def enterpassword(self,pwd):
        #self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(pwd)
        self.driver.find_element(*self.passwordlocator).send_keys(pwd)
        return self

    def login(self):
        #self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        from pages.homepage import Homepage
        self.driver.find_element(*self.loginlocator).click()
        return Homepage(self.driver)




