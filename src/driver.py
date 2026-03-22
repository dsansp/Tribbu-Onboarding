"""Driver manager for Appium sessions."""
from typing import Optional
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from appium.options.android import UiAutomator2Options
from config.capabilities import CapabilitiesConfig


class DriverManager:
    """Manages Appium driver lifecycle for Android devices."""
    
    _instance: Optional[WebDriver] = None
    
    def __init__(self, appium_url: str = "http://localhost:4723"):
        """Initialize DriverManager with Appium server URL.
        
        Args:
            appium_url: URL of the Appium server (default: http://localhost:4723)
        """
        self.appium_url = appium_url
    
    def create_driver(self, capabilities: CapabilitiesConfig) -> WebDriver:
        """Create a new Appium driver with given capabilities.
        
        Args:
            capabilities: CapabilitiesConfig instance with device/app settings
            
        Returns:
            WebDriver: Appium WebDriver instance
        """

        caps_dict = capabilities.to_dict()
        options = UiAutomator2Options().load_capabilities(caps_dict)
        self._instance = webdriver.Remote(
            command_executor=self.appium_url,
            options=options
        )
        return self._instance
    
    def get_driver(self) -> Optional[WebDriver]:
        """Get current driver instance.
        
        Returns:
            Optional[WebDriver]: Current driver or None if not initialized
        """
        return self._instance
    
    def quit_driver(self) -> None:
        """Quit the current driver session."""
        if self._instance:
            self._instance.quit()
            self._instance = None
    
    def __enter__(self) -> 'DriverManager':
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.quit_driver()