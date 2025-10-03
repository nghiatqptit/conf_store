#!/usr/bin/env python3
"""
Example usage of the configuration store.
"""

from config_store import ConfigStore


def main():
    # Create a config store instance
    config = ConfigStore("example_config.json")
    
    # Store some configuration
    config.set("database_host", "localhost")
    config.set("database_port", 5432)
    config.set("database_name", "myapp")
    config.set("debug_mode", True)
    config.set("api_keys", {
        "service1": "key123",
        "service2": "key456"
    })
    
    # Retrieve configuration
    print("Database host:", config.get("database_host"))
    print("Database port:", config.get("database_port"))
    print("Debug mode:", config.get("debug_mode"))
    print("API keys:", config.get("api_keys"))
    
    # Get with default value
    print("Max connections:", config.get("max_connections", 100))
    
    # Get all configuration
    print("\nAll configuration:")
    print(config.get_all())
    
    # Delete a key
    config.delete("debug_mode")
    print("\nAfter deleting debug_mode:")
    print(config.get_all())


if __name__ == "__main__":
    main()
