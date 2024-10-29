import random
from enum import Enum


class DeviceEnum(Enum):
    IPHONE_13 = (5, 10, 15, 25, 'Apple iPhone 13')
    IPHONE_14 = (5, 10, 15, 25, 'Apple iPhone 14')
    IPHONE_15 = (5, 10, 15, 25, 'Apple iPhone 15')

    GALAXY_S22 = (5, 10, 15, 25, 'Samsung Galaxy S22')
    GALAXY_S23 = (5, 10, 15, 25, 'Samsung Galaxy S23')
    GALAXY_S24 = (5, 10, 15, 25, 'Samsung Galaxy S24')

    PIXEL_6 = (5, 10, 15, 25, 'Google Pixel 6')
    ONEPLUS_9 = (5, 10, 15, 25, 'OnePlus 9')

    IPAD = (5, 10, 15, 25, 'Apple iPad')
    IPAD_PRO = (5, 10, 15, 25, 'Apple iPad Pro')
    GALAXY_TAB = (5, 10, 15, 25, 'Samsung Galaxy Tab')

    def __init__(self, signal_3g, signal_4g, signal_4glte, signal_5g, device_name):
        self.signals = {
            "3G": signal_3g,
            "4G": signal_4g,
            "4G LTE": signal_4glte,
            "5G": signal_5g
        }
        self.device_name = device_name

    def get_random_signal(self):
        signal_name = random.choice(list(self.signals.keys()))
        return signal_name, self.signals[signal_name]
