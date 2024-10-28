import numpy as np


class UserEquipment:
    def __init__(self, id, position, eq_class, status, sim_code, signal_power, ip_address, network_online):
        self.id = id  # User equipment ID
        self.position = position  # Position as (x, y) tuple
        self.connected_bs = None  # Connected base station
        self.eq_class = eq_class # device class(s24, ipad pro.. etc..
        self.new_position = None # temp new position when a device moves
        self.trajectory = [] # steps trajectory of the device
        self.status = status  # device power
        self.sim_code = sim_code # unique sim code for the device
        self.signal_power = signal_power # singal strength of the device
        self.ip_address = ip_address # ip of the device
        self.network_online = network_online  # Simulating online status (network) - if False no network connection will occur

    def signal_strength(self, user_position) -> int:
        my_array = np.array(user_position)
        distance = np.linalg.norm(self.position - my_array)
        return self.signal_power if distance == 0 else self.signal_power - 10 * np.log10(distance)

    def set_status(self, status) -> None:
        self.network_online = status
