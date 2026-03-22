from appium.webdriver.common.appiumby import AppiumBy
from .base_locators import BaseLocators

class DniLocators(BaseLocators):
    
    TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Gana dinero o viaja gratis con los Certificados de Ahorro Energético")')
    ACTIVAR_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Activar")')
    ACTIVAR_BUTTON_XPATH = (AppiumBy.XPATH, '//*[@text="Activar" or @content-desc="Activar"]')
    EDIT_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
    TOAST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.hoopcarpool.staging:id/snackbar_text")')
    TOAST_ERROR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.hoopcarpool.staging:id/snackbar_text")')
    BAD_EDIT_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("51704278W")')