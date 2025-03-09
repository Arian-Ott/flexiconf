import os
import json
import pytest
from pathlib import Path

@pytest.fixture
def config_data():
    """Provides a reusable test config dictionary."""
    return {
        "host": "127.0.0.1",
        "port": 8000,
        "debug": True
    }

@pytest.fixture
def temp_config_file(tmp_path, config_data):
    """Creates a temporary JSON config file with test data."""
    file_path = tmp_path / "config.json"
    with open(file_path, "w") as f:
        json.dump(config_data, f)
    return file_path

