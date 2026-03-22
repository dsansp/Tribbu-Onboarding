from appium.webdriver.common.appiumby import AppiumBy
from .base_locators import BaseLocators

class NameLocators(BaseLocators):
    OTP_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Necesitamos conocerte...")')
    TEXT_NAME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Introduce tu nombre")')
    EDIT_TEXT_NAME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
    SIGUIENTE_ALL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente")')
    LASTNAME_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Introduce tus apellidos")")')    
    EDIT_TEXT_LASTNAME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')