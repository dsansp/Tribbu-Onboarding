"""Page Object para las pantallas de Onboarding"""
from socket import timeout

from appium.webdriver.common.appiumby import AppiumBy

from src.pages import BasePage
from src.pages.locators.amigo_locators  import AmigoLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class AmigoPage(BasePage):
    """Página de Datos - Necesitamos conocerte..."""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_text_visible(self, timeout=20):
        """
        Espera al texto específico de la pagina sea visible."""
        locator = AmigoLocators.TEXT
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
   
    def enter_codigo_amigo(self, codigo):
       enteredCodigo = self.wait_for_element_visible(AmigoLocators.CODE_EDIT_TEXT, timeout=10)
       enteredCodigo.send_keys(codigo)
       print(f"✓ Código de amigo '{codigo}' ingresado")

    def verificar_Verificar_button_enabled(self):
            self.wait_button_10
            button = self.find_element_by_locator(AmigoLocators.VERIFICAR_BUTTON)
            button_enabled= button.get_attribute("clickable")=="true"
            print(f"Botón 'Verificar' enabled: {button_enabled}")
            return button_enabled
    
    def click_Verificar_button(self):
        try:
            self.wait(3)
            self.wait_for_element_clickable(AmigoLocators.VERIFICAR_BUTTON, timeout=10)
            self.click_element(AmigoLocators.VERIFICAR_BUTTON)
            print("✓ Botón 'Verificar' clicado")
            return True
        except TimeoutException:
            print(f"✗ No se encontró el botón 'Verificar' en {timeout}s")
            return False
    def get_toast_message(self, timeout=5):
        try:
            toast_element = self.wait_for_element_visible(AmigoLocators.TOAST, timeout=timeout)
            toast_message = toast_element.get_attribute("text")
            print(f"Mensaje del toast: '{toast_message}'")
            return toast_message
        except TimeoutException:
            print(f"✗ No se encontró el toast en {timeout}s")
            return None
   

   