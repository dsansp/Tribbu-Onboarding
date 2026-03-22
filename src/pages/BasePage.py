# src/pages/basepage.py
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

    def find_element_by_text(self, text, timeout=15):
        """Encuentra elemento por texto exacto (usando UiSelector o XPath)"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
        return self.driver.find_element(*locator)

    def find_element_by_text_contains(self, text, timeout=15):
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")')
        return self.driver.find_element(*locator)

    def find_element_by_locator(self, locator, timeout=15):
        return self.driver.find_element(*locator)
    
    def click_element(self, element):
        self.driver.find_element(*element).click()
    def get_element(self, locator, timeout=15):
        return self.driver.find_element(*locator)
    
    def wait(self, timeout=15):
            """Devuelve un WebDriverWait configurado con el driver de la página"""
            from selenium.webdriver.support.ui import WebDriverWait
            return WebDriverWait(self.driver, timeout)

    def wait_for_element_by_text(self, text, timeout=15):
        """Espera a que un elemento con texto específico esté presente"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')

        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator, timeout=15):
        """Espera a que un elemento sea clicable"""
        element= WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
    
    def wait_for_element_visible(self, locator, timeout=15):
        """Espera hasta que el elemento sea visible y lo retorna"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

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
        """Cuenta elementos que dentro de un localizador """
        main_element = driver.find_element(*locator)
        elements = main_element.find_elements(*locator)
        elements_count = len(elements)
        return elements_count
    
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



    def wait_for_element_clickable_except(self, locator, timeout=10, message=None):
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            msg = message or f"Elemento no clickable en {timeout}s: {locator}"
            raise TimeoutException(msg) from e
    
    def verificar_toast_message(self,toast_element, expected_message):
        try:
            actual_message = toast_element.text
            print(f"Toast actual: '{actual_message}' | Esperado: '{expected_message}'")
            return actual_message == expected_message
        except TimeoutException:
            print("✗ Toast NO visible para verificar mensaje")
            return False
    
    def verificar_color_snackbar(self, locator, r_target, g_target, b_target, savename):
        # 1. Esperar explícitamente a que el elemento aparezca
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
    
        # 2. CAPTURA INMEDIATA (Solo una vez)
        # Tomamos la captura justo después de encontrarlo
        img = Image.open(io.BytesIO(self.driver.get_screenshot_as_png()))
        
        # 3. Obtener escala y coordenadas
        scale = img.size[0] / self.driver.get_window_size()['width']
        location = element.location
        size = element.size
    
        left = int(location['x'] * scale)
        top = int(location['y'] * scale)
        right = int(left + (size['width'] * scale))
        bottom = int(top + (size['height'] * scale))
    
        # 4. Recorte y escaneo 
        im_crop = img.crop((left, top, right, bottom))
        im_crop.save(savename) 
        
        return self.es_color_presente(im_crop, r_target, g_target, b_target)
    
    def verificar_color_snackbar_element(self, element, r_target, g_target, b_target, savename):
       
        # 1. CAPTURA INMEDIATA (Solo una vez)
        # Tomamos la captura justo después de encontrarlo
        img = Image.open(io.BytesIO(self.driver.get_screenshot_as_png()))
        
        # 2. Obtener escala y coordenadas
        scale = img.size[0] / self.driver.get_window_size()['width']
        location = element.location
        size = element.size
    
        left = int(location['x'] * scale)
        top = int(location['y'] * scale)
        right = int(left + (size['width'] * scale))
        bottom = int(top + (size['height'] * scale))
    
        # 4. Recorte y escaneo 
        im_crop = img.crop((left, top, right, bottom))
        im_crop.save(savename) 
        
        return self.es_color_presente(im_crop, r_target, g_target, b_target)

    def es_color_presente(self, imagen_recortada, r_obj, g_obj, b_obj, tolerancia=40):
        img_rgb = imagen_recortada.convert('RGB')
        # Escaneamos los píxeles para buscar el verde del icono o del texto
        for x in range(0, img_rgb.size[0], 2): 
            for y in range(0, img_rgb.size[1], 2):
                r, g, b = img_rgb.getpixel((x, y))
                if abs(r - r_obj) < tolerancia and abs(g - g_obj) < tolerancia and abs(b - b_obj) < tolerancia:
                    print(f"✅ Verde detectado en píxel ({x},{y}): RGB({r},{g},{b})")
                    return True
        return False

    def verificar_color_snackbar_efimero(self, r_esperado, g_esperado, b_esperado, factor_pos=0.65, nombre_archivo="toast_check.png"):
        """
        Captura la pantalla completa inmediatamente para evitar el error de elemento Stale
        y analiza el color en la zona inferior (donde aparecen los Toasts).
        """
        path_screenshot = os.path.join("screenshots", nombre_archivo)
        os.makedirs("screenshots", exist_ok=True)
        
        # 1. Capturamos la pantalla completa YA (sin preguntar al elemento)
        self.driver.save_screenshot(path_screenshot)
        
        try:
            img = Image.open(path_screenshot)
            rgb_img = img.convert('RGB')
            
            # 2. En lugar de element.location, buscamos en una zona estimada
            # Los toasts suelen estar en la parte inferior central.
            width, height = img.size
            
            # Analizamos un punto específico (ej: 70% hacia abajo, centro)
            # Puedes ajustar estas coordenadas según tu dispositivo
            x = int(width / 2)
            y = int(height * factor_pos) 
            
            r, g, b = rgb_img.getpixel((x, y))
            print(f"DEBUG: Color detectado en ({x}, {y}): RGB({r},{g},{b})")
            
            # Margen de error de 10 unidades
            if abs(r - r_esperado) < 15 and abs(g - g_esperado) < 15 and abs(b - b_esperado) < 15:
                return True
            return False
        except Exception as e:
            print(f"Error analizando color: {e}")
            return False
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
