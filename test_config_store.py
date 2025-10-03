#!/usr/bin/env python3
"""
Simple test for the configuration store.
"""

import os
import tempfile
from config_store import ConfigStore


def test_config_store():
    """Test basic functionality of ConfigStore."""
    # Use a temporary file for testing
    test_file = os.path.join(tempfile.gettempdir(), "test_config.json")
    
    # Clean up any existing test file
    if os.path.exists(test_file):
        os.remove(test_file)
    
    # Test 1: Create new config store
    config = ConfigStore(test_file)
    assert config.get_all() == {}, "New config should be empty"
    
    # Test 2: Set and get values
    config.set("key1", "value1")
    assert config.get("key1") == "value1", "Should retrieve set value"
    
    # Test 3: Set different types
    config.set("number", 42)
    config.set("boolean", True)
    config.set("list", [1, 2, 3])
    config.set("dict", {"nested": "value"})
    
    assert config.get("number") == 42
    assert config.get("boolean") is True
    assert config.get("list") == [1, 2, 3]
    assert config.get("dict") == {"nested": "value"}
    
    # Test 4: Get with default
    assert config.get("nonexistent", "default") == "default"
    
    # Test 5: Delete key
    config.delete("key1")
    assert config.get("key1") is None
    
    # Test 6: Persistence - create new instance
    config2 = ConfigStore(test_file)
    assert config2.get("number") == 42, "Config should persist across instances"
    
    # Test 7: Get all
    all_config = config2.get_all()
    assert "number" in all_config
    assert "boolean" in all_config
    
    # Test 8: Clear
    config2.clear()
    assert config2.get_all() == {}, "Config should be empty after clear"
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("All tests passed! ✓")


if __name__ == "__main__":
    test_config_store()
