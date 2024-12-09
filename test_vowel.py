import pytest
from vowel import shorten


def test_shorten():
    assert shorten("aeiou") == ""
    assert shorten("twitter") == "twttr"
    
