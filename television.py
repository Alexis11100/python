


class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    def mute(self):
        if self.__status and self.__muted:
            self.__muted = False
        elif self.__status and not self.__muted:
            self.__muted = True





