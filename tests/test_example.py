"""Example test demonstrating Appium setup for Android physical device."""
import pytest
from src.app_launcher import AppLauncher
from src.driver import DriverManager
from config.capabilities import CapabilitiesConfig


class TestAndroidApp:
    """Example test class for Android app automation."""
    
    @pytest.fixture(scope="class")
    def app_launcher(self):
        """Fixture to provide AppLauncher instance."""
        launcher = AppLauncher(appium_url="http://localhost:4723")
        yield launcher
        launcher.close_app()
    
    @pytest.fixture(scope="class")
    def driver(self, app_launcher):
        """Fixture to create driver with specific app."""
        # Replace with your app's package name
        APP_ID = "com.hoopcarpool.staging"
        
        driver = app_launcher.launch_app(
            app_id=APP_ID
        )
        yield driver
    
    def test_app_launches_successfully(self, driver):
        """Test that app launches without errors."""
        assert driver is not None
        # Check if the current activity is running
        current_activity = driver.current_activity
        assert current_activity is not None
    
    def test_device_is_connected(self, driver):
        """Test that a physical device is connected."""
        # Get device capabilities
        capabilities = driver.desired_capabilities
        assert capabilities is not None
        assert "platformName" in capabilities
        assert capabilities["platformName"].lower() == "android"


# Example of standalone usage
if __name__ == "__main__":
    """Standalone example showing how to use the framework."""
    
    # Create capabilities configuration
    capabilities = CapabilitiesConfig.from_app_id(
        app_id="com.hoopcarpool.staging"  
    )
    
    # Optional: Set specific device UDID
    # capabilities.udid = "your-device-udid-here"
    
    # Create driver
    driver_manager = DriverManager()
    
    try:
        driver = driver_manager.create_driver(capabilities)
        print(f"App launched successfully!")
        print(f"Current activity: {driver.current_activity}")
        
        # Your test logic here
        
    finally:
        driver_manager.quit_driver()