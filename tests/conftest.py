# tests/conftest.py  
import pytest
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

    # Teardown: cierra bien (usa terminate_app si quieres mantener sesión viva, o quit)
    try:
        driver_instance.terminate_app("com.hoopcarpool.staging")  
    except:
        pass
    driver_instance.quit()  