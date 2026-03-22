"""Appium capabilities configuration for physical Android device."""
from dataclasses import dataclass, field
from typing import Optional
import json


@dataclass
class CapabilitiesConfig:
    """Configuration class for Appium capabilities on physical Android device.
    
    This class contains all the necessary capabilities to connect to a physical
    Android device via ADB and launch an installed application.
    
    Attributes:
        platform_name: Mobile platform (Android)
        device_name: Name/identifier of the device
        udid: Unique Device Identifier for the physical device
        app_package: Package name of the app (e.g., com.example.app)
        app_activity: Main activity to launch (e.g., .MainActivity)
        automation_name: Automation engine (UiAutomator2 for Android)
        no_reset: Whether to reset app state between sessions
        full_reset: Whether to do a full reset before/after session
        auto_grant_permissions: Auto grant app permissions
        ignore_unimportant_views: Ignore unimportant views for faster execution
        enable_performance_logging: Enable performance logging
    """
    
    platform_name: str = "Android"
    device_name: str = "45he4lcapvyldirg"
    udid: Optional[str] = "45he4lcapvyldirg"
    app_package: Optional[str] = None
    app_activity: Optional[str] = None
    automation_name: str = "UiAutomator2"
    no_reset: bool = True
    full_reset: bool = False
    auto_grant_permissions: bool = True
    ignore_unimportant_views: bool = True
    enable_performance_logging: bool = False
    new_command_timeout: int = 300
    auto_launch: bool = True
    
    def to_dict(self) -> dict:
        """Convert capabilities to dictionary format for Appium.
        
        Returns:
            dict: Capabilities in dictionary format
        """
        capabilities = {
            "platformName": self.platform_name,
            "deviceName": self.device_name,
            "automationName": self.automation_name,
            "noReset": self.no_reset,
            "fullReset": self.full_reset,
            "autoGrantPermissions": self.auto_grant_permissions,
            "ignoreUnimportantViews": self.ignore_unimportant_views,
            "newCommandTimeout": self.new_command_timeout,
            "autoLaunch": self.auto_launch,
        }
        
        if self.udid:
            capabilities["udid"] = self.udid
            
        if self.app_package:
            capabilities["appPackage"] = self.app_package
            
        if self.app_activity:
            capabilities["appActivity"] = self.app_activity
            
        if self.enable_performance_logging:
            capabilities["enablePerformanceLogging"] = self.enable_performance_logging
            
        return capabilities
    
    def to_json(self) -> str:
        """Convert capabilities to JSON string.
        
        Returns:
            str: JSON formatted capabilities
        """
        return json.dumps(self.to_dict(), indent=2)
    
    @classmethod
    def from_app_id(cls, app_id: str, udid: str = None, **kwargs) -> 'CapabilitiesConfig':
        """Create a CapabilitiesConfig instance from an app ID (package name).
        
        Args:
            app_id: The Android app package name (e.g., com.example.app)
            udid: Optional device UDID. If not provided, will use connected device.
            **kwargs: Additional optional arguments to override defaults
            
        Returns:
            CapabilitiesConfig: Configured instance for the specified app
        """
        return cls(
            app_package=app_id,
            udid=udid,
            **kwargs
        )
    
    def __str__(self) -> str:
        """String representation showing key capabilities."""
        return (
            f"CapabilitiesConfig(\n"
            f"  platform_name={self.platform_name},\n"
            f"  device_name={self.device_name},\n"
            f"  udid={self.udid},\n"
            f"  app_package={self.app_package},\n"
            f"  app_activity={self.app_activity},\n"
            f"  automation_name={self.automation_name}\n"
            f")"
        )