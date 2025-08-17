# Run the tests with: pytest tests/test_app.py
"""
Unit tests for the app module.

This module contains test cases for functions in the app module,
specifically testing the add_numbers function.
"""

import sys
from pathlib import Path

# Add the parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import add_numbers

def test_add_numbers():
    """
    Test add_numbers function with basic integer inputs
    """
    assert 3 == add_numbers(1,2)
