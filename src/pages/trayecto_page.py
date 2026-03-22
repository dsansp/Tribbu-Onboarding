"""Page Object para las pantallas de Onboarding"""
from socket import timeout

from appium.webdriver.common.appiumby import AppiumBy

from src.pages import BasePage
from src.pages.locators.trayecto_locators  import TrayectoLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class TrayectoPage(BasePage):
    """Página de Datos - Necesitamos conocerte..."""

    def __init__(self, driver):
        super().__init__(driver)

   
    def wait_text_trayecto_visible(self, timeout=20):
        """
        Espera al texto específico de la página y devuelve el texto encontrado.
        """
        locator = TrayectoLocators.TEXT
        try:
            self.wait(3) # Pausa opcional para estabilización
            # IMPORTANTE: Guardamos el elemento que devuelve la función de espera
            element = self.wait_for_element_visible(
                locator,
                timeout=timeout
            )
            print(f"✓ Texto de introducción visible")
            
            # Extraemos el texto del ELEMENTO, no del LOCATOR
            return element.text 
            
        except Exception as e: # Capturamos cualquier error (Timeout, etc)
            print(f"✗ Texto de introducción NO visible o error: {str(e)}")
            return False

   