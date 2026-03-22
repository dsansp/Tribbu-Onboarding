from appium.webdriver.common.appiumby import AppiumBy
from .base_locators import BaseLocators

class TypeUserLocators(BaseLocators):
    MAIN_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Empieza a compartir y ahorrar")')
    ENTRAR_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
    CONDUCTORS_BE_AMBAS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ambas").instance(0)')
    CONDUCTOR_BE_NO_SE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("No lo sé").instance(0)')
    CONDUCTORS_FOR_ME_AMBAS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ambas").instance(1)')
    ELEMENTOS_TYPE_USER = {AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(15)'}
    HIJOS_ELEMENTOS_TYPE_USER = (AppiumBy.XPATH,'./android.view.View')
    ENTRAR_BOX_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button")')
    ALLOW_NOTIFICATIONS_BUTTON = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')