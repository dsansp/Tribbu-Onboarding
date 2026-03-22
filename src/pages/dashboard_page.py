"""Page Object para las pantallas de Onboarding"""
from socket import timeout

from appium.webdriver.common.appiumby import AppiumBy

from src.pages import BasePage
from src.pages.locators.dashboard_menu_locators  import DashboardLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):
    """Página de Datos - Necesitamos conocerte..."""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_text_visible(self, timeout=20):
        """
        Espera al texto específico de la pagina sea visible."""
        locator = DashboardLocators.QUE_HACER_TEXT
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
   
    def click_Menu_button(self):
        self.wait_for_element_clickable(DashboardLocators.MENU_BUTTON, timeout=10)
        self.click_element(DashboardLocators.MENU_BUTTON)

   