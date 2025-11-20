import pytest
from television import Television

def test_init():
    tv = Television()
    # Use __str__ since variables are private
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # muted shows volume 0
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # unmuted restores volume
def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # wrap around
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()  # wrap from 0 to MAX_CHANNEL
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
