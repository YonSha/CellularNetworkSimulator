import numpy as np


class BaseStation:
    def __init__(self, id, position, power, status):
        self.id = id  # Base station ID
        self.position = position  # Position as (x, y) tuple
        self.power = power  # Transmission power in dBm
        self.status = status

    def signal_strength(self, user_position) -> int:
        distance = np.linalg.norm(self.position - user_position)
        return self.power if distance == 0 else self.power - 10 * np.log10(distance)
