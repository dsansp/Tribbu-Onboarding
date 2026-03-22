from appium.webdriver.common.appiumby import AppiumBy
from .base_locators import BaseLocators

class DashboardLocators(BaseLocators):
    QUE_HACER_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("¿Qué quieres hacer?")')
    
    MENU_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Menu")')
