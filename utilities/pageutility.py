from selenium.webdriver.support.select import Select


class Pageutility:
    def selectdata(self):
        sel = Select(dropdown)
        sel.select_by_value('staff')