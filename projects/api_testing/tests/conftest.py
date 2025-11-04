"""
This file contains a pytest fixture that can be shared across all test files and functions
in the project
"""

import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"