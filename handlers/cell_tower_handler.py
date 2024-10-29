import logging

import numpy as np
from base_classes.cell_tower import CellTower
from base_classes.cell_tower_with_position import CellTowerWithPosition


class CellTowerHandler(CellTower):

    def __init__(self, num_bs=1, provider_name=None, signal_strength=None, signal_type=None,supported_signals=None, id=None, position=None,
                 status=None):
        super().__init__(id, position, provider_name, signal_strength, signal_type,supported_signals, status)
        self.num_bs = num_bs
        self.provider_name = provider_name
        self.signal_type = signal_type
        self.signal_strength = signal_strength
        self.supported_signals = supported_signals
        self.bs_positions = np.random.rand(self.num_bs, 2) * 100  # random generic array
        self.cell_towers = [
            CellTower(id=i, position=pos, provider_name=self.provider_name, signal_strength=self.signal_strength, signal_type=self.signal_type, supported_signals=self.supported_signals,
                      status="online") for i, pos in
            enumerate(self.bs_positions)]

        self.stations_with_positions = [CellTowerWithPosition(bs, pos) for bs, pos in
                                        zip(self.cell_towers, self.bs_positions)]

    def add_cell_tower(self, provider=None, status="online"):
        signal_type, signal_strength = provider.get_random_signal_strength()
        id = len(self.cell_towers)
        bs_positions = np.random.rand(1, 2) * 100
        self.bs_positions = np.append(self.bs_positions, bs_positions, axis=0)
        temp_list = [CellTower(id=id, position=pos, provider_name=provider.provider_name,
                               signal_strength=signal_strength, signal_type=signal_type, supported_signals=provider.signals, status=status)
                     for i, pos in enumerate(bs_positions)]
        self.cell_towers += temp_list
        self.stations_with_positions = [CellTowerWithPosition(bs, pos) for bs, pos in
                                        zip(self.cell_towers, self.bs_positions)]
        logging.info(f"Added base station: id:{id}")

    def bs_go_offline(self, id) -> None:
        for bs in self.cell_towers:
            if bs.id == id:
                bs.status = "offline"

    def bs_go_online(self, id) -> None:
        for bs in self.cell_towers:
            if bs.id == id:
                bs.status = "online"

    def all_cpes_online(self) -> None:
        for bs in self.cell_towers:
            if bs.status == "offline":
                bs.status = "online"

    @property
    def bs_positions(self):
        return self._bs_positions

    @bs_positions.setter
    def bs_positions(self, value) -> None:
        self._bs_positions = value

    @property
    def return_bs_data(self):
        return self.cell_towers, self._bs_positions
