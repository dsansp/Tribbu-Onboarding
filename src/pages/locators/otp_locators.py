from appium.webdriver.common.appiumby import AppiumBy
from .base_locators import BaseLocators

class OtpLocators(BaseLocators):
    OTP_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Introduce el código de verificación")')
    EDIT_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
    SIGUIENTE_ALL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente")')
    TOAST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.hoopcarpool.staging:id/snackbar_text")')
    TOAST_COLOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(2)')
