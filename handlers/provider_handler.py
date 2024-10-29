import random


class ProviderHandler:

    def __init__(self, name, signals, status):
        super().__init__()
        self.__provider_name = name
        self.__signals = signals
        self.__status = status

    @property
    def provider_name(self):
        return self.__provider_name

    @property
    def signals(self):
        return self.__signals

    @property
    def status(self):
        return self.status

    def get_random_signal_strength(self):
        signal_type = random.choice(list(self.__signals.keys()))
        return signal_type, self.__signals[signal_type]
