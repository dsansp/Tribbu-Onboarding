# src/pages/basepage.py
import allure
from appium.webdriver.common.appiumby import AppiumBy
from src import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PIL import Image
import io
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Find element by text: {text}")
    def find_element_by_text(self, text, timeout=15):
        """Encuentra elemento por texto exacto (usando UiSelector o XPath)"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
        return self.driver.find_element(*locator)

    @allure.step("Find element containing text: {text}")
    def find_element_by_text_contains(self, text, timeout=15):
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")')
        return self.driver.find_element(*locator)

    @allure.step("Find element by locator")
    def find_element_by_locator(self, locator, timeout=15):
        return self.driver.find_element(*locator)
    
    @allure.step("Click element")
    def click_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step("Get element")
    def get_element(self, locator, timeout=15):
        return self.driver.find_element(*locator)
    
    def wait(self, timeout=15):
            """Devuelve un WebDriverWait configurado con el driver de la página"""
            from selenium.webdriver.support.ui import WebDriverWait
            return WebDriverWait(self.driver, timeout)

    @allure.step("Wait for element with text: {text}")
    def wait_for_element_by_text(self, text, timeout=15):
        """Espera a que un elemento con texto específico esté presente"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')

        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    @allure.step("Wait for element clickable and click")
    def wait_for_element_clickable(self, locator, timeout=15):
        """Espera a que un elemento sea clicable"""
        element= WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step("Wait for element visible")
    def wait_for_element_visible(self, locator, timeout=15):
        """Espera hasta que el elemento sea visible y lo retorna"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Wait for element presence")
    def wait_for_element(self, locator, timeout=15, message="Elemento no encontrado"):
        """Espera elemento con formato correcto Appium"""
        
        if isinstance(locator, (set, dict)):
            if len(locator) == 2:
                strategy, value = list(locator)
                if strategy.startswith('-android'):
                    strategy = AppiumBy.ANDROID_UIAUTOMATOR
                locator = (strategy, value)
            else:
                raise ValueError(f"Locator inválido: {locator}")
        
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except:
            raise Exception(message)

    def count_elements(self, locator, timeout=15):
        main_element = driver.find_element(*locator)
        elements = main_element.find_elements(*locator)
        elements_count = len(elements)
        return elements_count
    
    @allure.step("Check if button is enabled")
    def wait_button_enabled(self, locator, timeout=10):
        try:
            self.wait_for_element_clickable(locator, timeout=timeout)
            return True
        except:
            return False
            
    def wait_button_10(self, locator, timeout=10):
        try:
            self.wait_for_element_clickable(locator, timeout=timeout)
        except:
            pass

    @allure.step("Wait for element clickable with exception handling")
    def wait_for_element_clickable_except(self, locator, timeout=10, message=None):
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            msg = message or f"Elemento no clickable en {timeout}s: {locator}"
            raise TimeoutException(msg) from e
    
    def _crop_element_screenshot(self, element, savename, r_target, g_target, b_target):  
        img = Image.open(io.BytesIO(self.driver.get_screenshot_as_png()))

        scale = img.size[0] / self.driver.get_window_size()['width']
        location = element.location
        size = element.size
    
        left = int(location['x'] * scale)
        top = int(location['y'] * scale)
        right = int(left + (size['width'] * scale))
        bottom = int(top + (size['height'] * scale))

        im_crop = img.crop((left, top, right, bottom))
        im_crop.save(savename) 
        
        return self.es_color_presente(im_crop, r_target, g_target, b_target)
    
    def es_color_presente(self, imagen_recortada, r_obj, g_obj, b_obj, tolerancia=40):
        img_rgb = imagen_recortada.convert('RGB')

        for x in range(0, img_rgb.size[0], 2): 
            for y in range(0, img_rgb.size[1], 2):
                r, g, b = img_rgb.getpixel((x, y))
                if abs(r - r_obj) < tolerancia and abs(g - g_obj) < tolerancia and abs(b - b_obj) < tolerancia:
                    print(f"✅ Verde detectado en píxel ({x},{y}): RGB({r},{g},{b})")
                    return True
        return False

    @allure.step("Verify snackbar color RGB({r_esperado},{g_esperado},{b_esperado})")
    def verificar_color_snackbar_efimero(self, r_esperado, g_esperado, b_esperado, factor_pos=0.65, nombre_archivo="toast_check.png"):
        """
        Captura la pantalla completa inmediatamente para evitar el error de elemento Stale
        y analiza el color en la zona inferior (donde aparecen los Toasts).
        """
        path_screenshot = os.path.join("screenshots", nombre_archivo)
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot(path_screenshot)
        allure.attach.file(path_screenshot, name="Snackbar Screenshot", attachment_type=allure.attachment_type.PNG)
        
        try:
            img = Image.open(path_screenshot)
            rgb_img = img.convert('RGB')
            width, height = img.size
            x = int(width / 2)
            y = int(height * factor_pos) 
            r, g, b = rgb_img.getpixel((x, y))
            print(f"DEBUG: Color detectado en ({x}, {y}): RGB({r},{g},{b})")

            if abs(r - r_esperado) < 15 and abs(g - g_esperado) < 15 and abs(b - b_esperado) < 15:
                return True
            return False
        except Exception as e:
            print(f"Error analizando color: {e}")
            return False

    @allure.step("Scroll to text: {texto}")
    def scroll_to_text(self, texto):
        """Hace scroll hasta encontrar un elemento con el texto exacto."""
        try:
            selector = (
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                f'.scrollIntoView(new UiSelector().text("{texto}").instance(0))'
            )
            return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
        except Exception as e:
            print(f" No se pudo encontrar el texto '{texto}' tras el scroll: {e}")
            return None

    @allure.step("Get toast message")
    def getToast(self, element, timeout=30):
        try:
            self.wait_for_element_visible(element, timeout=10)
            toast_element = self.get_element(element)
            actual_message = toast_element.text
            print(f"Toast capturado: '{actual_message}'")
            return toast_element
        except TimeoutException:
            print("✗ Toast NO visible para obtener mensaje")
            return None