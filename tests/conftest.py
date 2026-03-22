# tests/conftest.py  
import pytest
import allure
from src.driver import DriverManager   
from src.app_launcher import AppLauncher  
from config.capabilities import CapabilitiesConfig


@pytest.fixture(scope="class")
def driver(request):
    """Fixture que crea y cierra el driver para tests de clase"""

    caps_config = CapabilitiesConfig.from_app_id(
        app_id="com.hoopcarpool.staging"   
    )

    driver_manager = DriverManager()
    driver_instance = driver_manager.create_driver(caps_config)  

    yield driver_instance

    try:
        driver_instance.terminate_app("com.hoopcarpool.staging")  
    except:
        pass
    driver_instance.quit()  

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == 'call' and rep.failed:
        try:
            if 'driver' in item.fixturenames:
                web_driver = item.funcargs['driver']
            
                allure.attach(
                    web_driver.get_screenshot_as_png(),
                    name="screenshot_error",
                    attachment_type=allure.attachment_type.PNG
                )
             
                try:
                    allure.attach(
                        web_driver.page_source,
                        name="page_source_error",
                        attachment_type=allure.attachment_type.HTML
                    )
                except Exception as e:
                    print(f"Error al capturar page source: {e}")
        except Exception as e:
            print(f"Error al capturar pantalla: {e}")
