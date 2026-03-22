from appium.webdriver.common.appiumby import AppiumBy
from .base_locators import BaseLocators

class AmigoLocators(BaseLocators):
    
    TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("¿Vienes de parte de un amigo?")')
    VERIFICAR_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Verificar")')
    CODE_EDIT_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    TOAST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.hoopcarpool.staging:id/snackbar_text")')