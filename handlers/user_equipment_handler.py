import numpy as np
from base_classes.user_equipment import UserEquipment


class UserEquipmentHandler(UserEquipment):

    def __init__(self, id=None, position=None, eq_class=None, status=None, bs_data=None, sim_code=None,
                 signal_strength=None, signal_name=None, ip_address=None, network_online=None):
        super().__init__(id, position, eq_class, status, sim_code, signal_strength, signal_name, ip_address,
                         network_online)
        self.trajectory = []
        self.base_stations, self.bs_positions = bs_data
        self.eq_list = []

    @property
    def return_eqs(self):
        return "sad"

    @property
    def bs_data(self):
        return self.base_stations, self.bs_positions

    def update_bs_data(self, bs_data) -> None:
        self.base_stations, self.bs_positions = bs_data

    def eq_go_online(self) -> None:
        self.connected_bs = True
        self.status = "online"

    def eq_go_offline(self) -> None:
        self.connected_bs = None
        self.status = "offline"

    def connect_to_bs(self, base_stations) -> None:
        # if cell tower not support the device current signal type or tower is offline, dont connect.
        base_stations = [bs for bs in base_stations if
                         bs.status != "offline" or self.signal_name not in bs.supported_signals]
        self.connected_bs = max(base_stations, key=lambda bs: bs.signal_strength_check(self.position)).id

    # returns the closest device or station ( not operational )
    def connect(self, base_stations, eqs) -> None:
        base_stations = [bs for bs in base_stations if bs.status != "offline"]
        eqs = [eq for eq in eqs if eq.status != "offline"]
        connected_bs = max(base_stations, key=lambda bs: bs.signal_strength_check(self.position)).id
        connected_eq = max(eqs, key=lambda eq: eq.signal_strength_check(self.position)).id
        if connected_eq > connected_bs:
            return connected_eq
        return connected_bs

    def move(self, num_steps) -> None:
        if self.status == "offline":
            print("the device is offline!")
        else:
            for step in range(num_steps):
                self.new_position = (self.position[0] + np.random.uniform(-20, 20),
                                     self.position[1] + np.random.uniform(-20, 20))
                self.position = self.new_position
                self.connect_to_bs(self.base_stations)
                self.trajectory.append((self.new_position, self.connected_bs))

    @property
    def return_trajectory(self) -> list:
        return self.trajectory

    @return_trajectory.setter
    def return_trajectory(self, value) -> None:
        self.trajectory = value

    '''
    def create_equipment(self, position, eq_class="mobile", status="online") -> [UserEquipment]:
        id=len(self.user_equipment_list) + 1
        return self.user_equipment_list.append(UserEquipment(id, position, eq_class,status))
    '''
