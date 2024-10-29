import numpy as np


class CellTower:
    def __init__(self, id, position,provider_name, signal_strength, signal_type,supported_signals, status):
        self.id = id  # Base station ID
        self.position = position  # Position as (x, y) tuple
        self.signal_strength = signal_strength  # Transmission power in dBm
        self.signal_type = signal_type
        self.status = status
        self.provider_name = provider_name
        self.supported_signals = supported_signals

    def signal_strength_check(self, user_position) -> int:
        distance = np.linalg.norm(self.position - user_position)
        return self.signal_strength if distance == 0 else self.signal_strength - 10 * np.log10(distance)
