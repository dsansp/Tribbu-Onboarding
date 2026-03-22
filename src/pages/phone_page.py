"""Page Object para las pantallas de Onboarding"""
import allure
from socket import timeout
from appium.webdriver.common.appiumby import AppiumBy
from src.pages import BasePage
from src.pages.locators.phone_locators import PhoneLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class PhonePage(BasePage):
    """Página de Phone - Introducción del número de teléfono"""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_text_visible(self, timeout=20):
        """
        Espera al texto específico de la pagina sea visible."""
        locator = PhoneLocators.PHONE_TEXT
        try:
            self.wait_for_element_visible(
                locator,
                timeout=timeout
            )
            print(f"✓ Texto de introducción visible")
            return True
        except TimeoutException:
            print(f"✗ Texto de introducción NO visible en {timeout}s")
            return False

    def check_checkbox(self, locator):
        self.wait(2)
        checkbox = self.wait_for_element_clickable(locator, timeout=30)
        
        if checkbox is None:
            print(f"→ Checkbox no encontrado o no clickable después de 30s: {locator}")
            return False  
        
        if not checkbox.is_selected():
            checkbox.click()
            print("→ Checkbox marcado")

        else:
            print("→ Checkbox ya estaba marcado")
    @allure.step("introduciendo el número de teléfono")
    def enter_phone_number(self, locator, phone_number):
        edit_text = self.wait_for_element_visible(locator, timeout=10)
        edit_text.send_keys(phone_number)
        print(f"✓ Número de teléfono '{phone_number}' ingresado")

    @allure.step("verificando que el checkbox esté marcado")
    def verificar_checkbox_marked(self, locator):
        self.driver.hide_keyboard()
        checkbox = self.find_element_by_locator(locator)
        is_checked = checkbox.get_attribute("checked") == "true"
        print(f"Checkbox marcado: {is_checked}")
        return is_checked
    def verificar_Siguiente_button_enabled(self):
        button = self.find_element_by_locator(PhoneLocators.SIGUIENTE_ALL_BUTTON)
        button_enabled= button.get_attribute("clickable")=="true"
        print(f"Botón 'Siguiente' enabled: {button_enabled}")
        return button_enabled
    
    def tap_Siguiente_button(self):
        self.wait_for_element_clickable(PhoneLocators.SIGUIENTE_ALL_BUTTON_BUTTON, timeout=10)
        self.click_element(PhoneLocators.SIGUIENTE_ALL_BUTTON)