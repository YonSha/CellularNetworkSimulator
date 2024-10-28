from enum import Enum


class DeviceEnum(Enum):
    IPHONE_12 = (60, 'Apple iPhone 12')
    IPHONE_13 = (55, 'Apple iPhone 13')
    IPHONE_14 = (50, 'Apple iPhone 14')
    IPHONE_15 = (45, 'Apple iPhone 15')

    GALAXY_S21 = (50, 'Samsung Galaxy S21')
    GALAXY_S22 = (48, 'Samsung Galaxy S22')
    GALAXY_S23 = (46, 'Samsung Galaxy S23')
    GALAXY_S24 = (44, 'Samsung Galaxy S24')

    PIXEL_6 = (45, 'Google Pixel 6')
    ONEPLUS_9 = (40, 'OnePlus 9')

    IPAD = (35, 'Apple iPad')
    IPAD_PRO = (38, 'Apple iPad Pro')
    GALAXY_TAB = (30, 'Samsung Galaxy Tab')
    SURFACE_PRO = (32, 'Microsoft Surface Pro')

    def __init__(self, signal_strength, device_name):
        self.signal_strength = signal_strength
        self.device_name = device_name
