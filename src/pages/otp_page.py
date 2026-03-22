"""Page Object para las pantallas de Onboarding"""
from socket import timeout

from appium.webdriver.common.appiumby import AppiumBy

from src.pages import BasePage
from src.pages.locators.otp_locators import OtpLocators
from src.pages.locators.phone_locators import PhoneLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class OtpPage(BasePage):
    """Página de OTP - Introducción del código de verificación"""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_text_visible(self, timeout=20):
        """
        Espera al texto específico de la pagina sea visible."""
        locator = OtpLocators.OTP_TEXT
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
   
    def enter_Otp_number(self, locator, otp_number):
        edit_text = self.wait_for_element_visible(locator, timeout=10)
        edit_text.send_keys(otp_number)
        print(f"✓ Código de verificación '{otp_number}' ingresado")

    def verificar_checkbox_marked(self, locator):
        checkbox = self.find_element_by_locator(locator)
        is_checked = checkbox.get_attribute("checked") == "true"
        print(f"Checkbox marcado: {is_checked}")
        return is_checked
    def verificar_Siguiente_button_enabled(self):
        self.wait_button_10
        button = self.find_element_by_locator(OtpLocators.SIGUIENTE_ALL_BUTTON)
        button_enabled= button.get_attribute("clickable")=="true"
        print(f"Botón 'Siguiente' enabled: {button_enabled}")
        return button_enabled
    
    def tap_Siguiente_button(self):
        self.wait_for_element_clickable(OtpLocators.SIGUIENTE_ALL_BUTTON, timeout=10)
        self.click_element(OtpLocators.SIGUIENTE_ALL_BUTTON)

    def waitToastVisible(self, timeout=30):
        try:
            self.wait_for_element_visible(OtpLocators.TOAST, timeout=timeout)
            print("✓ Toast visible")
            return True
        except TimeoutException:
            print("✗ Toast NO visible en {timeout}s")
            return False
        
    # def getToast(self, timeout=30):
    #     try:
    #         self.wait_for_element_visible(OtpLocators.TOAST, timeout=10)
    #         toast_element = self.get_element(OtpLocators.TOAST)
    #         actual_message = toast_element.text
    #         print(f"Toast capturado: '{actual_message}'")
    #         return toast_element
    #     except TimeoutException:
    #         print("✗ Toast NO visible para obtener mensaje")
    #         return None

    def verificar_toast_color(self, expected_color):
       
            toast_element = self.wait_for_element_visible(OtpLocators.TOAST, timeout=10)
            try:
                bg = toast_element.get_attribute("background")  
                print(f"background: {bg}") 
            except:
                pass   
            try:
                color_attr = toast_element.get_attribute("backgroundColor") 
                print(f"backgroundColor: {color_attr}")
            except:
                pass 
            try:
                actual_color = toast_element.value_of_css_property("background-color")
                print(f"actual-color: {actual_color}")
            except:
                pass 
            
            return  expected_color
