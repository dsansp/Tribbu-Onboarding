from appium.webdriver.common.appiumby import AppiumBy
from .base_locators import BaseLocators

class MenuLocators(BaseLocators):
    
    ELIMINAR_CUENTA_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Eliminar cuenta")')
    PERFIL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Mi perfil")')
    CONFIRMATION_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    CONFIRM_ERASE= (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Si, Eliminar")')