import pytest
from television import Television

def test_init():
    tv = Television()
    # Use __str__ since variables are private
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"