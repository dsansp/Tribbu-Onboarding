from appium.webdriver.common.appiumby import AppiumBy
from .base_locators import BaseLocators

class PhoneLocators(BaseLocators):
    PHONE_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Te enviaremos un SMS, pero no se compartirá con nadie.")')
    CHECK = (AppiumBy.CLASS_NAME, "android.widget.CheckBox")
    EDIT_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    SIGUIENTE_ALL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)')

