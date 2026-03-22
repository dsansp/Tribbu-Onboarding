"""Page Object para las pantallas de Onboarding"""
from socket import timeout

from appium.webdriver.common.appiumby import AppiumBy

from src.pages import BasePage
from src.pages.locators.type_user_locators import TypeUserLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class OnboardingPage(BasePage):
    """Página de Onboarding - Pasos del flujo de bienvenida"""

    def __init__(self, driver):
        super().__init__(driver)

    def verificar_views_visibles(self, inicio, fin, timeout=12):
        """
        Verifica que las vistas (instance N a M) sean visibles.
        Devuelve True si TODAS están visibles, False en caso contrario.
        """
        total = fin - inicio           
        visibles = 0

        print(f"→ Verificando {total} vistas: instance({inicio}) a instance({fin}) ...")

        for i in range(inicio, fin ):
            locator = (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().className("android.view.View").instance({i})'
            )
            try:
                elemento = self.wait_for_element_visible(
                    locator,
                    timeout=timeout
                )
                print(f"  ✓ instance({i:2d}) visible")
                visibles += 1
            except TimeoutException:
                print(f"  ✗ instance({i:2d}) NO visible en {timeout}s")

        exito = visibles == total
        print(f"Resultado final: {visibles}/{total} visibles → {'OK' if exito else 'FALLO'}")
        return exito



    def get_type_user_options_count(self):
        """
        Cuenta cuántos elementos (opciones/botones) están cargados en la pantalla de tipo de usuario.
        Retorna la cantidad como entero.
        """
        # 1. Espera a que la pantalla esté visible 
        self.wait_for_element(TypeUserLocators.MAIN_TEXT, timeout=20)
    

        container_locator = TypeUserLocators.ELEMENTOS_TYPE_USER   
        
        container = self.wait_for_element(
            container_locator,
            timeout=15,
            message="No se encontró el contenedor de opciones en la pantalla de tipo de usuario"
        )
        
        # 2 Cuenta los elementos dentro del contenedor
        locator= TypeUserLocators.HIJOS_ELEMENTOS_TYPE_USER
        if isinstance(locator, set):
            locator = tuple(locator)  
        buttons = container.find_elements(locator)
        
        count = len(buttons)
        
       
        print(f"Se encontraron {count} botones/opciones en el contenedor") 
        
        return count

    def select_driver_actions(self):
        self.wait_for_element_clickable(TypeUserLocators.CONDUCTOR_BE_NO_SE, timeout=10)

               
    def select_travel_actions(self): 
        self.wait_for_element_clickable(TypeUserLocators.CONDUCTORS_FOR_ME_AMBAS, timeout=10)
      


    def verificar_Entrar_button_enabled(self):
        button = self.find_element_by_locator(TypeUserLocators.ENTRAR_BOX_BUTTON)
        button_enabled= button.get_attribute("clickable")=="true"
        print(f"Botón 'Entrar' enabled: {button_enabled}")
        return button_enabled
    
    def tap_Entrar_button(self):
        self.wait_for_element_clickable(TypeUserLocators.ENTRAR_BUTTON, timeout=10)

    def allow_notifications(self):
        possible_locators = [
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button'),
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'),
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button_background'),  
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Permitir")'),  
        ]
        
        for locator in possible_locators:
            try:
                button = self.wait_for_element_clickable_except(locator, timeout=5)
                button.click()
                print(f"→ Permitido usando: {locator}")
                return  
            except TimeoutException:
                print(f"  → No encontrado: {locator}")
                continue
        
        print("→ Ningún botón 'Permitir' encontrado → se omite")