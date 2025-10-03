"""
A simple configuration store module for storing and retrieving configuration data.
"""

import json
import os
from typing import Any, Dict, Optional


class ConfigStore:
    """A simple configuration store that can save and load configuration data."""
    
    def __init__(self, config_file: str = "config.json"):
        """
        Initialize the configuration store.
        
        Args:
            config_file: Path to the configuration file (default: config.json)
        """
        self.config_file = config_file
        self._config: Dict[str, Any] = {}
        self.load()
    
    def load(self) -> None:
        """Load configuration from file if it exists."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    self._config = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._config = {}
        else:
            self._config = {}
    
    def save(self) -> None:
        """Save current configuration to file."""
        with open(self.config_file, 'w') as f:
            json.dump(self._config, f, indent=2)
    
    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self._config[key] = value
        self.save()
    
    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key doesn't exist
            
        Returns:
            The configuration value or default
        """
        return self._config.get(key, default)
    
    def delete(self, key: str) -> None:
        """
        Delete a configuration key.
        
        Args:
            key: Configuration key to delete
        """
        if key in self._config:
            del self._config[key]
            self.save()
    
    def get_all(self) -> Dict[str, Any]:
        """
        Get all configuration data.
        
        Returns:
            Dictionary containing all configuration
        """
        return self._config.copy()
    
    def clear(self) -> None:
        """Clear all configuration data."""
        self._config = {}
        self.save()
