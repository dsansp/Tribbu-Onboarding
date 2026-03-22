"""Page Object para las pantallas de Onboarding"""
from socket import timeout

from appium.webdriver.common.appiumby import AppiumBy

from src.pages import BasePage
from src.pages.locators.dni_locators  import DniLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class DniCertificadosPage(BasePage):
    """Página de Datos - Necesitamos conocerte..."""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_text_visible(self, timeout=20):
        """
        Espera al texto específico de la pagina sea visible."""
        locator = DniLocators.TEXT
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
   
    def enter_dni(self, dni):
       enteredDni = self.wait_for_element_visible(DniLocators.EDIT_TEXT, timeout=10)
       enteredDni.send_keys(dni)
       print(f"✓ DNI '{dni}' ingresado")

    def clear_dni_field(self):
        """Limpia el campo de DNI de forma segura"""
        element = self.driver.find_element(*DniLocators.EDIT_TEXT)
        element.clear()  
        if element.text != "":
            self.driver.execute_script('mobile: replaceElementValue', {
            'elementId': element.id, 
            'text': ''})
        print("✓ Campo DNI limpiado")

    def verificar_Activar_button_enabled(self):
            self.wait(3)
            button = self.find_element_by_locator(DniLocators.ACTIVAR_BUTTON_XPATH)
            button_enabled= button.get_attribute("clickable")=="true"
            print(f"Botón 'Activar' enabled: {button_enabled}")
            return button_enabled
    def check_Activar_button_enabled(self, timeout=10):
        try:
            self.wait_for_element_clickable(DniLocators.ACTIVAR_BUTTON_XPATH, timeout=timeout)
            print(f"✓ Botón 'Activar' habilitado en {timeout}s")
            return True
        except TimeoutException:
            print(f"✗ Botón 'Activar' NO habilitado en {timeout}s")
            return False
    def click_Activar_button(self):
        try:
            self.wait(3)
            self.wait_for_element_clickable(DniLocators.ACTIVAR_BUTTON_XPATH, timeout=10)
            self.click_element(DniLocators.ACTIVAR_BUTTON_XPATH)
            print("✓ Botón 'Activar' clicado")
            return True
        except TimeoutException:
            print(f"✗ No se encontró el botón 'Activar' en {timeout}s")
            return False
    # def get_toast_message(self, timeout=5):
    #     try:
    #         toast_element = self.wait_for_element_visible(DniLocators.TOAST, timeout=timeout)
    #         toast_message = toast_element.get_attribute("text")
    #         print(f"Mensaje del toast: '{toast_message}'")
    #         return toast_message
    #     except TimeoutException:
    #         print(f"✗ No se encontró el toast en {timeout}s")
    #         return None
    # def getToast(self, timeout=30):
    #     try:
    #         self.wait_for_element_visible(DniLocators.TOAST, timeout=10)
    #         toast_element = self.get_element(DniLocators.TOAST)
    #         actual_message = toast_element.text
    #         print(f"Toast capturado: '{actual_message}'")
    #         return toast_element
    #     except TimeoutException:
    #         print("✗ Toast NO visible para obtener mensaje")
    #         return None
   