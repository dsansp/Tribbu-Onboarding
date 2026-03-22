"""Page Object para las pantallas de Onboarding"""
from socket import timeout

from appium.webdriver.common.appiumby import AppiumBy

from src.pages import BasePage
from src.pages.locators.name_locators  import NameLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class NamesPages(BasePage):
    """Página de Datos - Necesitamos conocerte..."""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_text_visible(self, timeout=20):
        """
        Espera al texto específico de la pagina sea visible."""
        locator = NameLocators.OTP_TEXT
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
   
    def verificar_Siguiente_button_enabled(self):
        self.wait_button_10
        button = self.find_element_by_locator(NameLocators.SIGUIENTE_ALL_BUTTON)
        button_enabled= button.get_attribute("clickable")=="true"
        print(f"Botón 'Siguiente' enabled: {button_enabled}")
        return button_enabled
    
    def enter_name(self,  name):
        edit_text = self.wait_for_element_visible(NameLocators.EDIT_TEXT_NAME, timeout=10)
        edit_text.send_keys(name)
        print(f"✓ Nombre '{name}' ingresado")
    
    def enter_lastname(self,  lastname):
        edit_text = self.wait_for_element_visible(NameLocators.EDIT_TEXT_LASTNAME, timeout=10)
        edit_text.send_keys(lastname)
        print(f"✓ Apellidos '{lastname}' ingresados")

    def verificar_name(self, expected_name):
        edit_text = self.wait_for_element_visible(NameLocators.EDIT_TEXT_NAME, timeout=30)
        actual_name = edit_text.get_attribute("text")
        print(f"Nombre actual: '{actual_name}' | Esperado: '{expected_name}'")
        return actual_name == expected_name
    
    def verificar_lastname(self, expected_lastname):
        edit_text = self.wait_for_element_visible(NameLocators.EDIT_TEXT_LASTNAME, timeout=30)
        actual_lastname = edit_text.get_attribute("text")
        print(f"Apellido actual: '{actual_lastname}' | Esperado: '{expected_lastname}'")
        return actual_lastname == expected_lastname