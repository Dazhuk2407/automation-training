# pytest configuration and shared fixtures

import pytest
from pathlib import Path


@pytest.fixture
def project_root():
    """Get project root directory"""
    return Path(__file__).parent.absolute()


@pytest.fixture
def data_dir(project_root):
    """Get test data directory"""
    data = project_root / "test_data"
    data.mkdir(exist_ok=True)
    return data


def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as unit test"
    )

