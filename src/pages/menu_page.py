"""Page Object para las pantallas de Onboarding"""
from socket import timeout

from appium.webdriver.common.appiumby import AppiumBy

from src.pages import BasePage
from src.pages.locators.menu_locators  import MenuLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class MenuPage(BasePage):
    """Página de Datos - Necesitamos conocerte..."""

    def __init__(self, driver):
        super().__init__(driver)

   
    def click_Perfil_button(self):
        self.wait_for_element_clickable(MenuLocators.PERFIL_BUTTON, timeout=10)
        self.click_element(MenuLocators.PERFIL_BUTTON)

    def click_Eliminar_cuenta_button(self):
        self.scroll_to_text("Eliminar cuenta")
        self.wait_for_element_clickable(MenuLocators.ELIMINAR_CUENTA_BUTTON, timeout=10)
        self.click_element(MenuLocators.ELIMINAR_CUENTA_BUTTON)
   
    def introduccir_confirmacion_eliminar_cuenta(self,text, timeout=10):
        self.wait_for_element_visible(MenuLocators.CONFIRMATION_TEXT, timeout=timeout)
        edit_text = self.find_element_by_locator(MenuLocators.CONFIRMATION_TEXT)
        edit_text.send_keys(text)
        print(f"✓ Confirmación '{text}' ingresada")

    def confirmar_eliminar_cuenta(self):
        self.wait_for_element_clickable(MenuLocators.CONFIRM_ERASE, timeout=10)
        self.click_element(MenuLocators.CONFIRM_ERASE)
