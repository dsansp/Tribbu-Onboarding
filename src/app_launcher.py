"""App launcher module for Android applications."""
from typing import Optional
from appium.webdriver.webdriver import WebDriver
from config.capabilities import CapabilitiesConfig
from .driver import DriverManager


class AppLauncher:
    """Handles launching Android apps on physical devices via Appium."""
    
    def __init__(self, appium_url: str = "http://localhost:4723"):
        """Initialize AppLauncher with Appium server URL.
        
        Args:
            appium_url: URL of the Appium server
        """
        self.driver_manager = DriverManager(appium_url)
        self._driver: Optional[WebDriver] = None
    
    def launch_app(self, app_id: str, udid: Optional[str] = None, 
                   app_activity: Optional[str] = None) -> WebDriver:
        """Launch an Android app by its package name.
        
        Args:
            app_id: Android app package name (e.g., com.example.app)
            udid: Optional device UDID for specific device
            app_activity: Optional main activity (defaults to .MainActivity)
            
        Returns:
            WebDriver: Appium WebDriver instance
        """
        capabilities = CapabilitiesConfig.from_app_id(
            app_id=app_id,
            udid=udid
        )
        
        if app_activity:
            capabilities.app_activity = app_activity
            
        self._driver = self.driver_manager.create_driver(capabilities)
        return self._driver
    
    def close_app(self) -> None:
        """Close the current app and quit driver."""
        if self._driver:
            try:
                self._driver.terminate_app(self._driver.current_package)
            except Exception as e:
                print(f"Error al cerrar app: {e}")
            finally:
                self._driver = None
    
    @property
    def driver(self) -> Optional[WebDriver]:
        """Get current WebDriver instance."""
        return self._driver