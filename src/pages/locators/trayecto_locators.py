from appium.webdriver.common.appiumby import AppiumBy
from .base_locators import BaseLocators

class TrayectoLocators(BaseLocators):
    
    TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Publica tu primer trayecto y haz match con otras personas")')
