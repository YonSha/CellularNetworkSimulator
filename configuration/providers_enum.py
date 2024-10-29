import random
from enum import Enum


class ProviderEnum(Enum):
    customer_one = ("Provider One", {"3G": 50}, "active")
    customer_two = ("Provider Two", {"3G": 45, "4G": 55, "5G": 65}, "active")

    def __init__(self, provider_name, signals, status):
        self.__provider_name = provider_name
        self.__signals = signals
        self.__status = status

    @property
    def provider_name(self):
        return self.__provider_name

    @property
    def status(self):
        return self.__status

    @property
    def signals(self):
        return self.__signals

    def get_random_signal_strength(self):
        signal_type = random.choice(list(self.__signals.keys()))
        return signal_type, self.__signals[signal_type]
