from selenium import webdriver


class InitWebDriver:

    @staticmethod
    def Init_web_driver():
        web_driver = webdriver.Chrome("driver_interactions/chromedriver.exe")
        return web_driver
