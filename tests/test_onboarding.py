"""Test de Onboarding basado en onboarding-tribbu-maestro.yaml"""
from threading import Thread
import allure
import pytest
from src.app_launcher import AppLauncher
from src.pages import otp_page
from src.pages.amigo_page import AmigoPage
from src.pages.dashboard_page import DashboardPage
from src.pages.dni_certificados_page import DniCertificadosPage
from src.pages.locators.dni_locators import DniLocators
from src.pages.locators.name_locators import NameLocators
from src.pages.locators.type_user_locators import TypeUserLocators
from src.pages.locators.phone_locators import PhoneLocators
from src.pages.locators.otp_locators import OtpLocators
from src.pages.locators.amigo_locators import AmigoLocators
from src.pages.menu_page import MenuPage
from src.pages.names_page import NamesPages
from src.pages.onboarding_page import OnboardingPage
from src.pages.otp_page import OtpPage
from src.pages.phone_page import PhonePage
from src.pages.dni_generator import generate_valid_dni
from src.pages.trayecto_page import TrayectoPage


@pytest.mark.onboarding
@allure.epic("Onboarding de Usuario")
@allure.feature("Flujo de Onboarding")
@allure.story("Registro completo de nuevo usuario")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
        Este test verifica:
        1. El flujo hasta iniciar un trayecto por primera vez.
        2. La validación de un DNI repetido.
        3. La validación de un código de amigo.
        4. El mensaje y color del toast después de cada validación.
        5. La validacion del OTP.
        6. La correcta carga de todos los elementos esperados.
    """)
class TestOnboarding:
    """Tests para el flujo de Onboarding"""

    def app_launcher(self):
        """Fixture to provide AppLauncher instance."""
        launcher = AppLauncher(appium_url="http://localhost:4723")
        yield launcher
        launcher.close_app()
    

    def driver(self, app_launcher):
        """Fixture to create driver with specific app."""
        APP_ID = "com.hoopcarpool.staging"
        
        driver = app_launcher.launch_app(
            app_id=APP_ID
        )
    
    def test_complete_onboarding(self, driver):  
        """Verifica que el flujo de onboarding se completa correctamente"""
        onboarding_page = OnboardingPage(driver)
        phone_page = PhonePage(driver)
        otp_page = OtpPage(driver)
        names_page = NamesPages(driver)
        dni_page = DniCertificadosPage(driver)
        amigo_page = AmigoPage(driver)
        trayecto_page = TrayectoPage(driver)
        onboarding_page.allow_notifications() 
        dni_repetido = "51704278W"
        otp_pass = "111111"    

        with allure.step("Seleccionar tipo de usuario y acciones"):
            assert onboarding_page.verificar_views_visibles(16, 25) == True, \
            "No se encontraron todas las opciones esperadas en la pantalla de tipo de usuario"
            assert onboarding_page.verificar_Entrar_button_enabled() == False, "El botón 'Entrar' habilitado antes de seleccionar opciones"
            onboarding_page.select_driver_actions()
            onboarding_page.wait(2)  
            assert onboarding_page.verificar_Entrar_button_enabled() == False, "El botón 'Entrar' habilitado antes de seleccionar opciones"
            onboarding_page.select_travel_actions()
            assert onboarding_page.wait_button_enabled(TypeUserLocators.ENTRAR_BOX_BUTTON, timeout=10) == True, "El botón 'Entrar' no se habilitó después de seleccionar opciones"  # Espera breve para que se actualice el estado del botón

        with allure.step("Ingresar número de teléfono"):
            assert phone_page.wait_text_visible(timeout=15)
            assert phone_page.check_checkbox(PhoneLocators.CHECK) == False, "El checkbox no se pudo marcar o ya estaba marcado"
            assert phone_page.verificar_checkbox_marked(PhoneLocators.CHECK) == True, "El checkbox no está marcado después de intentar marcarlo"
            
            assert phone_page.verificar_Siguiente_button_enabled() == False, "El botón 'Siguiente' habilitado antes de ingresar número"
            
            phone_page.enter_phone_number(PhoneLocators.EDIT_TEXT, "3214678950")
            phone_page.wait_button_enabled(PhoneLocators.SIGUIENTE_ALL_BUTTON, timeout=5)
            assert phone_page.wait_button_enabled(PhoneLocators.SIGUIENTE_ALL_BUTTON, timeout=15) == True, "El botón 'Siguiente' no se habilitó después de ingresar número"

        with allure.step("Verificar código OTP"):
            assert otp_page.wait_text_visible(timeout=15)
            assert otp_page.verificar_Siguiente_button_enabled() == False, "El botón 'Siguiente' habilitado antes de ingresar número"

            otp_page.enter_Otp_number(OtpLocators.EDIT_TEXT, otp_pass )
            otp_page.wait_button_10
            
            assert otp_page.wait_button_enabled(OtpLocators.SIGUIENTE_ALL_BUTTON, timeout=15) == True, "El botón 'Siguiente' no se habilitó después de ingresar el OTP"
            
            mensaje_toast = otp_page.getToast(OtpLocators.TOAST, timeout=15).text 
            print(f"Toast capturado: {mensaje_toast}")
            es_verde = otp_page.verificar_color_snackbar_efimero(208, 239, 223, 0.65, "otp_snackbar.png")
            assert mensaje_toast == "Código verificado correctamente", f"Mensaje inesperado: {mensaje_toast}"
            assert es_verde, "El snackbar no tiene el color verde esperado"

        with allure.step("Ingresar nombre y apellidos"):
            assert names_page.wait_text_visible(timeout=15)

            assert names_page.verificar_Siguiente_button_enabled() == False, "El botón 'Siguiente' habilitado antes de ingresar número"
            names_page.enter_name("Pedro")  
            names_page.wait_button_10
            assert names_page.verificar_name("Pedro")

            assert names_page.verificar_Siguiente_button_enabled() == False, "El botón 'Siguiente' habilitado antes de ingresar número"
            names_page.enter_lastname("Picapiedra")  
            names_page.wait_button_10
            assert names_page.verificar_lastname("Picapiedra")

            assert names_page.wait_button_enabled(NameLocators.SIGUIENTE_ALL_BUTTON, timeout=15) == True, "El botón 'Siguiente' no se habilitó después de ingresar los nombres y apellidos"

        with allure.step("Validar DNI repetido y luego ingresar DNI válido"):
            dni_page.wait_text_visible(timeout=20)
            assert dni_page.verificar_Activar_button_enabled() == False, "El botón 'Activar' habilitado antes de ingresar el DNI"
            dni_page.enter_dni(dni_repetido)
            dni_page.wait(4)
            assert dni_page.check_Activar_button_enabled() == True, "El botón 'Activar' no se habilitó después de ingresar el DNI"
            dni_page.click_Activar_button()
            mensaje_toast_dni = dni_page.getToast(DniLocators.TOAST, timeout=15).text 
            assert mensaje_toast_dni == 'El número de DNI o NIE que has utilizado ya está asociado a un usuario. Si crees que se trata de un error, ponte en contacto con soporte haciendo clic en el icono de "?" para solucionarlo'  # Verifica que el mensaje del toast de error sea el esperado

        
            new_dni = generate_valid_dni()
            print(f"Generando nuevo DNI para prueba: {new_dni}")

            dni_page.clear_dni_field()
            dni_page.enter_dni(new_dni)
                  
            assert dni_page.click_Activar_button() == True, "El botón 'Activar' no se habilitó después de ingresar el DNI"

        with allure.step("Ingresar código de amigo"):
            assert amigo_page.wait_text_visible(timeout=20)
            amigo_page.enter_codigo_amigo("MARIOM-0956")
            assert amigo_page.click_Verificar_button() == True, "El botón 'Verificar' no se habilitó después de ingresar el código de amigo"
            mensaje_toast_amigo = amigo_page.getToast(AmigoLocators.TOAST, timeout=15).text 
            amigo_es_verde = otp_page.verificar_color_snackbar_efimero(208, 239, 223, 0.9, "amigo_snackbar.png")
            assert mensaje_toast_amigo == "Código verificado correctamente", f"Mensaje inesperado: {mensaje_toast}"
            assert amigo_es_verde, "El snackbar no tiene el color verde esperado"


        with allure.step("Verificar finalización del onboarding"):
            print("✓ Flujo de onboarding completado exitosamente")
        

            try:
                Goal_indicator_text = trayecto_page.wait_text_trayecto_visible(timeout=20)
                assert Goal_indicator_text == "Publica tu primer trayecto y haz match con otras personas", "No se completó el onboarding - no llegó a la pantalla de trayecto"
            except:
                pytest.fail("No se encontró indicador de pantalla de destino después del onboarding")

    
     
