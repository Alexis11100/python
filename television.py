


class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        """
         Initialize the Television with default values.

         Private instance variables:
         - __status (bool): Power status, initially False (off).
         - __muted (bool): Mute status, initially False (unmuted).
         - __volume (int): Current volume, initially MIN_VOLUME.
         - __channel (int): Current channel, initially MIN_CHANNEL.
         """
        self.__status:bool = False
        self.__muted:bool = False
        self.__volume:int = Television.MIN_VOLUME
        self.__channel:int = Television.MIN_CHANNEL
    def power(self) -> None:
        """Toggle the TV power on/off."""
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    def mute(self) -> None:
        """Toggle mute/unmute, but only if the TV is on."""
        if self.__status and self.__muted:
            self.__muted = False
        elif self.__status and not self.__muted:
            self.__muted = True
    def channel_up(self) -> None:
        """Increase the channel by 1, wrapping to MIN_CHANNEL if at MAX_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    def channel_down(self) -> None:
        """Decrease the channel by 1, wrapping to MAX_CHANNEL if at MIN_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    def volume_up(self) -> None:
        """Increase the volume by 1, unmuting if necessary. Does nothing if at MAX_VOLUME."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    def volume_down(self) -> None:
        """Decrease the volume by 1, unmuting if necessary. Does nothing if at MIN_VOLUME."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    def __str__(self) -> str:
        """
        Return a string representation of the TV state.
        If muted, volume is displayed as 0.
        """
        volume_display = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"









