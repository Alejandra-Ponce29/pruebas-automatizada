from driver_interactions.Elementsinteractions import ElementsInteractions
from driver_interactions.InitWebDriver import InitWebDriver
import time


def before_all(context):
    context.prepare_driver = InitWebDriver()
    context.web_driver = context.prepare_driver.Init_web_driver()
    context.interactions_object = ElementsInteractions(context.web_driver)
    context.interactions_object.launch_web_page("www.saucedemo.com")


def after_all(context):
    time.sleep(5)
    context.web_driver.quit()



