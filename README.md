# conf_store

A simple configuration store for storing and retrieving configuration data.

## Features

- Store and retrieve configuration values
- Persistent storage using JSON format
- Simple key-value interface
- Support for nested configuration (dictionaries)
- Default values for missing keys

## Usage

```python
from config_store import ConfigStore

# Create a config store instance
config = ConfigStore("config.json")

# Store configuration
config.set("database_host", "localhost")
config.set("database_port", 5432)
config.set("api_keys", {"service1": "key123"})

# Retrieve configuration
host = config.get("database_host")
port = config.get("database_port")

# Get with default value
max_conn = config.get("max_connections", 100)

# Get all configuration
all_config = config.get_all()

# Delete a configuration key
config.delete("database_port")

# Clear all configuration
config.clear()
```

## Example

Run the example script to see the config store in action:

```bash
python example.py
```