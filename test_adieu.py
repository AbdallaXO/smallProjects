import pytest
from adieu import adieu_format

def test_adieu_format():
    names = ["Abdi", "Anna", "Bob"]
    result = adieu_format(names)
    expected = "Adieu, adieu, to Abdi, Anna, and Bob"
    assert result == expected